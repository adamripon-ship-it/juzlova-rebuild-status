import type { Config, Context } from "@netlify/functions"

const CONTACT_TO_DEFAULT = "juzlj@seznam.cz"
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
const LANGS = ["cs", "en", "de", "sk"] as const
const SUBJECT: Record<(typeof LANGS)[number], string> = {
  cs: "Jůzlová — poptávka z webu",
  en: "Jůzlová — website enquiry",
  de: "Jůzlová — Anfrage über die Website",
  sk: "Jůzlová — dopyt z webu",
}

interface ContactBody {
  name?: unknown
  phone?: unknown
  email?: unknown
  message?: unknown
  products?: unknown
  lang?: unknown
  turnstileToken?: unknown
  honeypot?: unknown
}

interface ValidPayload {
  name: string
  phone: string
  email: string
  message: string
  products: string[]
  lang: (typeof LANGS)[number]
  turnstileToken: string
  honeypot: string
}

const env = (name: string) => {
  const fromNetlify = typeof Netlify !== "undefined" ? Netlify.env.get(name) : undefined
  return (fromNetlify || process.env[name] || "").trim()
}

const json = (data: unknown, status = 200) =>
  new Response(JSON.stringify(data), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
    },
  })

const timedFetch = (url: string, init: RequestInit, ms = 10000) =>
  fetch(url, { ...init, signal: AbortSignal.timeout(ms) })

const clip = (value: unknown, max: number) =>
  String(value ?? "").replace(/\r/g, "").trim().slice(0, max)

const isLang = (value: string): value is (typeof LANGS)[number] =>
  (LANGS as readonly string[]).includes(value)

const isLocalDev = () => {
  const context = env("CONTEXT")
  const url = env("URL") || env("DEPLOY_PRIME_URL")
  return context === "dev" || env("NETLIFY_DEV") === "true" || /localhost|127\.0\.0\.1/.test(url)
}

const parseBody = (raw: unknown): ValidPayload | { error: string } => {
  if (!raw || typeof raw !== "object") return { error: "invalid" }
  const body = raw as ContactBody
  const name = clip(body.name, 200)
  const phone = clip(body.phone, 40)
  const email = clip(body.email, 200)
  const message = clip(body.message, 4000)
  const langRaw = clip(body.lang, 8).toLowerCase()
  const lang = isLang(langRaw) ? langRaw : "cs"
  const honeypot = clip(body.honeypot, 200)
  const turnstileToken = clip(body.turnstileToken, 4000)
  const products = Array.isArray(body.products)
    ? body.products.map((item) => clip(item, 120)).filter(Boolean).slice(0, 12)
    : []

  if (!name || !email) return { error: "invalid" }
  if (!EMAIL_RE.test(email)) return { error: "invalid" }

  return { name, phone, email, message, products, lang, turnstileToken, honeypot }
}

const formatMail = (payload: ValidPayload) => {
  const lines = [
    SUBJECT[payload.lang],
    "",
    `Jméno / Name: ${payload.name}`,
    payload.phone ? `Telefon / Phone: ${payload.phone}` : "",
    `E-mail: ${payload.email}`,
    payload.products.length ? `Směsi / Mixes: ${payload.products.join(", ")}` : "",
    payload.message ? `Zpráva / Message:\n${payload.message}` : "",
  ]
  return lines.filter((line, i) => line || i === 1).join("\n")
}

const verifyTurnstile = async (token: string, ip: string) => {
  const secret = env("TURNSTILE_SECRET_KEY")
  if (!secret) return { ok: true, skipped: true }
  if (!token) return { ok: false, skipped: false }

  const body = new URLSearchParams()
  body.set("secret", secret)
  body.set("response", token)
  if (ip) body.set("remoteip", ip)

  let res: Response
  try {
    res = await timedFetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: body.toString(),
    })
  } catch {
    return { ok: false, skipped: false }
  }
  if (!res.ok) return { ok: false, skipped: false }
  const data = (await res.json()) as { success?: boolean; hostname?: string; action?: string }
  if (!data.success) return { ok: false, skipped: false }

  const allowed = env("TURNSTILE_HOSTNAMES")
  if (allowed) {
    const hosts = new Set(allowed.split(",").map((h) => h.trim().toLowerCase()).filter(Boolean))
    const hostname = String(data.hostname || "").toLowerCase()
    if (hosts.size && hostname && !hosts.has(hostname)) return { ok: false, skipped: false }
  }

  if (data.action && data.action !== "contact") return { ok: false, skipped: false }
  return { ok: true, skipped: false }
}

const isZapierHook = (url: string) => {
  try {
    const parsed = new URL(url)
    return parsed.protocol === "https:" && (
      parsed.hostname === "hooks.zapier.com" ||
      parsed.hostname.endsWith(".hooks.zapier.com")
    )
  } catch {
    return false
  }
}

const sendZapier = async (payload: ValidPayload) => {
  const hook = env("ZAPIER_WEBHOOK_URL")
  if (!isZapierHook(hook)) return false

  const to = env("CONTACT_TO") || CONTACT_TO_DEFAULT
  try {
    const res = await timedFetch(hook, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        to,
        subject: SUBJECT[payload.lang],
        name: payload.name,
        phone: payload.phone,
        email: payload.email,
        message: payload.message,
        products: payload.products.join(", "),
        lang: payload.lang,
        body: formatMail(payload),
      }),
    })
    return res.ok
  } catch {
    return false
  }
}

const handleGet = () =>
  json({
    siteKey: env("TURNSTILE_SITE_KEY") || null,
  })

const handlePost = async (req: Request, context: Context) => {
  let raw: unknown
  try {
    raw = await req.json()
  } catch {
    return json({ ok: false, error: "invalid" }, 400)
  }

  const parsed = parseBody(raw)
  if ("error" in parsed) return json({ ok: false, error: parsed.error }, 400)

  if (parsed.honeypot) return json({ ok: true })

  const captcha = await verifyTurnstile(parsed.turnstileToken, context.ip || "")
  if (!captcha.ok) return json({ ok: false, error: "captcha" }, 403)

  if (await sendZapier(parsed)) return json({ ok: true, mode: "zapier" })
  if (isLocalDev()) return json({ ok: true, mode: "dev" })
  return json({ ok: false, error: "mail" }, 502)
}

export default async (req: Request, context: Context) => {
  switch (req.method) {
    case "GET":
      return handleGet()
    case "POST":
      return handlePost(req, context)
    case "OPTIONS":
      return new Response(null, {
        status: 204,
        headers: {
          "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type, Accept",
          "Cache-Control": "no-store",
        },
      })
    default:
      return json({ ok: false, error: "method_not_allowed" }, 405)
  }
}

export const config: Config = {
  path: ["/api/contact", "/.netlify/functions/contact"],
  method: ["GET", "POST", "OPTIONS"],
}
