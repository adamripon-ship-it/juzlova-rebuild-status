import { createHash } from "node:crypto"
import { getStore } from "@netlify/blobs"
import type { Config, Context } from "@netlify/functions"

const SLUGS = [
  "sisky-s-makem-recept",
  "hruskovy-kolac-s-vanilkovym-pudinkem-recept",
  "strapacky-se-zelim-a-slaninou-recept",
  "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem",
  "slehackova-rolada-recept",
  "domaci-pernik-recept-podle-jirina-juzlova",
  "bramborovo-tvarohove-knedliky-s-jahodami",
  "rychle-venecky-ci-vetrnicky-recept",
  "venecky-s-vanilkovym-kremem-recept",
  "kremrole-recept",
  "minivetrnicky-recept",
  "karamelove-vetrniky-recept",
  "irsky-sticky-toffee-pudding-recept",
] as const

type RecipeSlug = (typeof SLUGS)[number]

interface RecipeRow {
  sum_tenths: number
  count: number
}

interface RatingsDoc {
  version: 1
  recipes: Record<string, RecipeRow>
}

const SEED: RatingsDoc = {
  version: 1,
  recipes: {
    "sisky-s-makem-recept": { sum_tenths: 4089, count: 87 },
    "hruskovy-kolac-s-vanilkovym-pudinkem-recept": { sum_tenths: 2880, count: 64 },
    "strapacky-se-zelim-a-slaninou-recept": { sum_tenths: 4416, count: 92 },
    "podle-lucie-kuzelovebebe-rezy-s-cokoladovym-pudingem": { sum_tenths: 3124, count: 71 },
    "slehackova-rolada-recept": { sum_tenths: 2585, count: 55 },
    "domaci-pernik-recept-podle-jirina-juzlova": { sum_tenths: 4410, count: 98 },
    "bramborovo-tvarohove-knedliky-s-jahodami": { sum_tenths: 3648, count: 76 },
    "rychle-venecky-ci-vetrnicky-recept": { sum_tenths: 2332, count: 53 },
    "venecky-s-vanilkovym-kremem-recept": { sum_tenths: 3807, count: 81 },
    "kremrole-recept": { sum_tenths: 3105, count: 69 },
    "minivetrnicky-recept": { sum_tenths: 2784, count: 58 },
    "karamelove-vetrniky-recept": { sum_tenths: 4136, count: 94 },
    "irsky-sticky-toffee-pudding-recept": { sum_tenths: 2914, count: 62 },
  },
}

const STORE_KEY = "recipe-ratings"
const VOTE_PREFIX = "vote:"

const isSlug = (value: string): value is RecipeSlug =>
  (SLUGS as readonly string[]).includes(value)

const json = (data: unknown, status = 200) =>
  new Response(JSON.stringify(data), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
    },
  })

const store = () => getStore({ name: "juzlova-ratings", consistency: "strong" })

const publicRow = (row: RecipeRow) => ({
  ratingValue: Number((row.sum_tenths / 10 / row.count).toFixed(1)),
  ratingCount: row.count,
  bestRating: 5,
  worstRating: 1,
})

const publicAll = (doc: RatingsDoc) => {
  const recipes: Record<string, ReturnType<typeof publicRow>> = {}
  for (const slug of SLUGS) {
    const row = doc.recipes[slug] ?? SEED.recipes[slug]
    recipes[slug] = publicRow(row)
  }
  return { version: 1, recipes }
}

const loadDoc = async (): Promise<RatingsDoc> => {
  const blob = store()
  const existing = await blob.get(STORE_KEY, { type: "json" }) as RatingsDoc | null
  if (existing && existing.recipes && typeof existing.recipes === "object") {
    const merged: RatingsDoc = { version: 1, recipes: { ...SEED.recipes } }
    for (const slug of SLUGS) {
      const row = existing.recipes[slug]
      if (row && Number.isFinite(row.sum_tenths) && Number.isFinite(row.count) && row.count > 0) {
        merged.recipes[slug] = {
          sum_tenths: Math.round(row.sum_tenths),
          count: Math.round(row.count),
        }
      }
    }
    return merged
  }
  await blob.setJSON(STORE_KEY, SEED)
  return structuredClone(SEED)
}

const fingerprint = (req: Request, slug: string) => {
  const ip = req.headers.get("x-nf-client-connection-ip")
    || req.headers.get("x-forwarded-for")?.split(",")[0]?.trim()
    || "unknown"
  const ua = req.headers.get("user-agent") || ""
  return createHash("sha256").update(`${ip}|${ua}|${slug}`).digest("hex").slice(0, 32)
}

const handleGet = async (slug: string | undefined) => {
  const doc = await loadDoc()
  if (!slug) return json(publicAll(doc))
  if (!isSlug(slug)) return json({ error: "unknown_recipe" }, 404)
  return json({ slug, ...publicRow(doc.recipes[slug]) })
}

const handlePost = async (req: Request, slug: string | undefined) => {
  if (!slug || !isSlug(slug)) return json({ error: "unknown_recipe" }, 404)
  let stars = 0
  try {
    const body = await req.json() as { stars?: unknown }
    stars = Number(body.stars)
  } catch {
    return json({ error: "invalid" }, 400)
  }
  if (!Number.isInteger(stars) || stars < 1 || stars > 5) {
    return json({ error: "invalid_stars" }, 400)
  }

  const blob = store()
  const voteKey = VOTE_PREFIX + fingerprint(req, slug)
  const already = await blob.get(voteKey)
  if (already) {
    const doc = await loadDoc()
    return json({ slug, already: true, ...publicRow(doc.recipes[slug]) })
  }

  const doc = await loadDoc()
  const row = doc.recipes[slug]
  row.sum_tenths += stars * 10
  row.count += 1
  await blob.setJSON(STORE_KEY, doc)
  await blob.set(voteKey, String(stars), {
    metadata: { slug, at: new Date().toISOString() },
  })
  return json({ slug, already: false, ...publicRow(row) })
}

export default async (req: Request, context: Context) => {
  const slug = (context.params?.slug || "").replace(/\/+$/, "")
  switch (req.method) {
    case "GET":
      return handleGet(slug || undefined)
    case "POST":
      return handlePost(req, slug || undefined)
    default:
      return json({ error: "method" }, 405)
  }
}

export const config: Config = {
  path: ["/api/ratings", "/api/ratings/:slug"],
}
