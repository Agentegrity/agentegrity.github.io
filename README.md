# Agentegrity

**Verifiable integrity for AI agents.** Marketing site for Agentegrity — a Cogensec project that gives the agentic enterprise runtime attestation, behavioral guardrails, and tamper-evident audit for every AI agent and tool call.

🔗 **Live site:** https://cogensec.github.io/agentegrity.github.io/

## About

Agentegrity governs the decision-to-action boundary of autonomous AI systems — proving, in real time, that every agent acts with integrity. The site is a single, self-contained static page with no build step and no external dependencies.

## Project structure

| File | Purpose |
| --- | --- |
| `index.html` | The full landing page (HTML, CSS, and JS inlined) |
| `404.html` | Branded not-found page |
| `.nojekyll` | Serves files as-is, bypassing Jekyll processing |
| `robots.txt` / `sitemap.xml` | Basic SEO |

## Local preview

No tooling required — open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8080
# then visit http://localhost:8080
```

## Publishing with GitHub Pages

1. Push these files to the branch GitHub Pages serves from (typically `main`).
2. In **Settings → Pages**, set **Source** to *Deploy from a branch* and choose that branch with the `/ (root)` folder.
3. GitHub builds and serves the site within a minute or two.

### Custom domain (optional)

To serve from a custom domain (e.g. `agentegrity.com`), add a `CNAME` file containing the domain and configure the DNS record with your provider.

## License

© Cogensec. All rights reserved.
