#!/usr/bin/env python3
"""Summarize a private order ledger; no uploads or automatic purchase events."""
import argparse
import csv
from collections import defaultdict
from decimal import Decimal, InvalidOperation

AI = {'chatgpt', 'perplexity', 'claude', 'gemini', 'copilot'}

def summarize(rows):
    totals = defaultdict(lambda: {'orders': 0, 'net_revenue_czk': Decimal('0')})
    seen = set()
    basis = set()
    for row in rows:
        order_id = row['order_id'].strip()
        if not order_id: raise ValueError('Missing order_id')
        if order_id in seen: raise ValueError('Duplicate order_id: ' + order_id)
        seen.add(order_id)
        status = row['status'].strip()
        if status not in {'quoted', 'accepted', 'paid', 'cancelled', 'refunded', 'partially_refunded'}:
            raise ValueError('Unknown order status: ' + status)
        if status in {'quoted', 'accepted', 'cancelled'}: continue
        if row['currency'] != 'CZK': raise ValueError('Report requires CZK')
        if row['revenue_basis'] not in {'including_vat', 'excluding_vat'}: raise ValueError('Specify revenue_basis')
        basis.add(row['revenue_basis'])
        if len(basis) > 1: raise ValueError('Mixed VAT bases')
        try:
            value, refund = Decimal(row['order_value']), Decimal(row.get('refund_value') or '0')
        except InvalidOperation as exc: raise ValueError('Invalid money value') from exc
        if not value.is_finite() or not refund.is_finite() or not 0 <= refund <= value:
            raise ValueError('Invalid order/refund amount')
        if status == 'refunded' and value != refund: raise ValueError('Full refund must equal order value')
        observed = row.get('observed_ai_source', '').strip().lower()
        reported = row.get('self_reported_ai_source', '').strip().lower()
        source = observed if observed in AI else reported if reported in AI else 'unknown_or_other'
        method = 'observed' if observed in AI else 'self_reported' if reported in AI else 'unknown_or_other'
        group = totals[(source, method)]
        group['orders'] += 1
        group['net_revenue_czk'] += value - refund
    return [{'source': s, 'attribution_method': m, **v} for (s, m), v in sorted(totals.items())]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('orders_csv'); parser.add_argument('report_csv')
    args = parser.parse_args()
    with open(args.orders_csv, newline='', encoding='utf-8-sig') as f:
        results = summarize(csv.DictReader(f))
    with open(args.report_csv, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['source', 'attribution_method', 'orders', 'net_revenue_czk'])
        writer.writeheader(); writer.writerows(results)
