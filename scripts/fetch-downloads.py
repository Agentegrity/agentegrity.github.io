#!/usr/bin/env python3
"""Fetch the all-time "Total downloads" scalar from the public PyPI ClickHouse
Metabase dashboard and write it to downloads.json for the site to read.

The dashboard is public, so no auth is needed. We query the single "Total
downloads" card (card 642 / dashcard 582 on dashboard
8d516106-3a9f-4674-aafc-aa39d6380ee2) with the project_name filter pinned to
"agentegrity".
"""
import datetime
import json
import pathlib
import sys
import urllib.parse
import urllib.request

HOST = "https://clickhouse-analytics.metabaseapp.com"
DASHBOARD = "8d516106-3a9f-4674-aafc-aa39d6380ee2"
DASHCARD_ID = 582
CARD_ID = 642
PROJECT = "agentegrity"

# Parameter mapping taken from the dashboard's parameter_mappings for this card.
PARAMS = [
    {
        "id": "483d46b6",
        "type": "string/=",
        "target": ["dimension", ["field", 531, {"base-type": "type/Text"}], {"stage-number": 0}],
        "value": PROJECT,
    }
]


def fetch_total():
    qs = urllib.parse.urlencode({"parameters": json.dumps(PARAMS)})
    url = f"{HOST}/api/public/dashboard/{DASHBOARD}/dashcard/{DASHCARD_ID}/card/{CARD_ID}?{qs}"
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/json", "User-Agent": "agentegrity-site/1.0"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        payload = json.load(resp)

    rows = payload.get("data", {}).get("rows") or []
    if not rows or rows[0] is None or rows[0][0] is None:
        sys.stderr.write("Unexpected response shape:\n")
        sys.stderr.write(json.dumps(payload)[:1000] + "\n")
        raise SystemExit(1)
    return int(rows[0][0])


def main():
    total = fetch_total()
    out = {
        "total": total,
        "source": "metabase",
        "project": PROJECT,
        "updated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    pathlib.Path("downloads.json").write_text(json.dumps(out) + "\n")
    print(f"Wrote downloads.json: total={total}")


if __name__ == "__main__":
    main()
