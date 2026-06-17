# agentegrity.github.io

Marketing site for **Agentegrity** — _structural integrity for intelligent agents_. A Cogensec Research initiative.

> Agentegrity (agent + integrity) is the discipline of building AI agents that can defend, stabilize, and recover themselves — and then cryptographically verifying that they actually can.

🔗 **Live site:** https://cogensec.github.io/agentegrity.github.io/

## About this repo

This repository contains the static landing page only. It is a single, self-contained
`index.html` (HTML + CSS + a small amount of vanilla JS, no build step). The page supports
a light/dark theme toggle that persists to `localStorage`, and uses the Geist typeface.

| File | Purpose |
| --- | --- |
| `index.html` | The full landing page |
| `404.html` | Branded not-found page |
| `assets/cogensec-emblem.png` | Cogensec wordmark emblem |
| `.nojekyll` | Serves files as-is, bypassing Jekyll processing |
| `robots.txt` / `sitemap.xml` | Basic SEO |

## Local preview

No tooling required — open `index.html` directly, or serve the folder:

```bash
python3 -m http.server 8080
# then visit http://localhost:8080
```

## Publishing with GitHub Pages

1. Push these files to the branch GitHub Pages serves from (typically `main`).
2. In **Settings → Pages**, set **Source** to *Deploy from a branch* and pick that branch with the `/ (root)` folder.
3. The site builds and serves within a minute or two.

### Custom domain (optional)

To serve from a custom domain, add a `CNAME` file containing the domain (e.g. `agentegrity.cogensec.com`)
and create the matching DNS record with your provider.

## License

© Cogensec Research. The Agentegrity framework is released under Apache-2.0.
