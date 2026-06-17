# agentegrity.github.io

Marketing site for **Agentegrity** — _structural integrity for intelligent agents_. A Cogensec Research initiative.

> Agentegrity (agent + integrity) is the discipline of building AI agents that can defend, stabilize, and recover themselves — and then cryptographically verifying that they actually can.

🔗 **Live site:** https://agentegrity.github.io/

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

## Publishing at `https://agentegrity.github.io/`

GitHub serves a repository at `https://<account>.github.io/` only when the repo is named
`<account>.github.io` **and** is owned by an account named `<account>`. To reach the root
domain `https://agentegrity.github.io/`, this repo must live under a GitHub account named
`agentegrity` (the name is currently unregistered):

1. Create a GitHub **organization** named `agentegrity` (a free org is fine).
2. **Transfer** this repository into it (repo *Settings → General → Transfer ownership*), or
   create a new `agentegrity.github.io` repo there and push these files. The repo path
   becomes `agentegrity/agentegrity.github.io`.
3. Put the site on the **`main`** branch.
4. In **Settings → Pages**, set **Source** to *Deploy from a branch* → `main` / `/ (root)`.
5. The site builds and serves at `https://agentegrity.github.io/` within a minute or two.

> While it stays under the `cogensec` org, GitHub publishes it as a project site at
> `https://cogensec.github.io/agentegrity.github.io/` instead.

### Custom domain (optional)

To serve from your own domain instead, add a `CNAME` file containing the domain
(e.g. `agentegrity.cogensec.com`) and create the matching DNS record with your provider.

## License

© Cogensec Research. The Agentegrity framework is released under Apache-2.0.
