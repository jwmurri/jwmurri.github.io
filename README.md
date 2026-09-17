# jwmurri.com

A Quarto site. Pages are Markdown (`.qmd`), styling lives in one stylesheet,
and pushing to `main` rebuilds and deploys it.

## One-time setup

1. **Install Quarto** — <https://quarto.org/docs/get-started/>. On macOS,
   `brew install --cask quarto` works too.

2. **Make a repo.** On GitHub, create a repository named `jwmurri.github.io`
   (that exact name lets the site live at the root of your GitHub Pages
   account). Then, in this folder:

   ```bash
   git init
   git add .
   git commit -m "Initial site"
   git branch -M main
   git remote add origin git@github.com:<your-username>/jwmurri.github.io.git
   git push -u origin main
   ```

3. **Turn on Pages.** In the repo: Settings → Pages → Build and deployment →
   Source → **GitHub Actions**. The workflow in `.github/workflows/publish.yml`
   handles the rest; every push to `main` rebuilds the site.

4. **Point the domain at it.** In Settings → Pages → Custom domain, enter
   `jwmurri.com`. Then, at whatever registrar holds the domain, set:

   - an `ALIAS`/`ANAME` record, or four `A` records for the apex, pointing to
     `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - a `CNAME` record for `www` pointing to `<your-username>.github.io`

   DNS takes an hour or so to settle. Once it has, tick "Enforce HTTPS".
   Keep the `CNAME` file in this folder — it is what tells Pages which domain
   to serve.

   Google Sites will keep serving the domain until you remove the custom-domain
   mapping in Google Sites settings, so do that when you're ready to cut over.

## Working on it

```bash
quarto preview     # live-reloading local server; edits show up as you save
quarto render      # one-off build into _site/
```

`_site/` is generated output and is gitignored. Don't edit it.

## What's where

| File | What it is |
|---|---|
| `index.qmd` | The About page |
| `research.qmd`, `papers.qmd`, `teaching.qmd` | The other pages |
| `_masthead.html` | Name, header graphic, and nav — appears on every page |
| `_footer.html` | Contact line at the bottom of every page |
| `_head.html` | Font loading |
| `custom.scss` | All the styling |
| `_quarto.yml` | Site config — title, metadata, which files to include |
| `cv.pdf` | **Placeholder.** Replace with your actual CV. |
| `CNAME` | The custom domain, read by GitHub Pages |
| `tools/gen_header_trace.py` | Regenerates the header graphic |

## Adding a page

Create `talks.qmd` with front matter at the top:

```yaml
---
title: "Talks"
pagetitle: "Talks — Jacob Murri"
---
```

Then add a link to it in `_masthead.html`. That's the whole process — Quarto
picks up any `.qmd` in the folder.

## Math

LaTeX works inline with `$...$` and display with `$$...$$`; Quarto renders it
with MathJax. See `research.qmd` for an example.

## The header graphic

Two trajectories of the Lorenz '63 system. The red one is the truth; the blue
one starts from a different initial condition and is nudged toward it using
observations of a single component, so it converges onto the red one partway
across. The curves are real numerical output, not decoration —
`tools/gen_header_trace.py` computes them and prints SVG path data that gets
pasted into `_masthead.html`. Change `mu`, `T`, or the plotted component there
and regenerate if you want a different figure.

To drop the graphic entirely, delete the `<figure class="trace">` block from
`_masthead.html`.

## Notes

- Colours and type sizes are all CSS custom properties at the top of
  `custom.scss`. Change them in one place.
- Dark mode follows the reader's system setting.
- The `<!-- ... -->` comments in the `.qmd` files mark the spots that still
  need your content. They don't show up on the page.
