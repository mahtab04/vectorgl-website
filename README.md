# VectorGL website

This is a static website. HTML, CSS and browser JavaScript are served directly;
there is no frontend build step, framework, external font or CDN dependency.

## Preview locally

From the repository root:

```sh
python -m http.server 8765 --directory site
```

Open <http://localhost:8765/>. The Pages workflow validates the site on pull requests and deploys `site/`
when changes land on `main`. In repository Settings → Pages, select
**GitHub Actions** as the source before the first deployment.

## Editing the site

- `index.html`: introduction, Canvas/Scene/UI examples and CMake integration.
- `overview.html`: architecture, build profiles and installation.
- `guides.html`: lifecycle examples and links to detailed guides.
- `examples.html`: screenshot gallery and runnable repository examples.
- `api.html`: searchable reference, populated from `app.js`.
- `styles.css`: shared responsive layout, light/dark themes and focus styles.
- `app.js`: reference data, syntax highlighting, search, code tabs and copying.

Keep the main content and navigation usable without JavaScript. Search, theme
switching and code tabs enhance the static pages. Code blocks must be keyboard
focusable so users can scroll long lines on small screens. Respect reduced motion
and verify both themes at mobile and desktop widths after layout changes.

Screenshots in `images/` show actual repository examples. `ui-workspace.png` was
captured from `vectorgl_ui_editor_workspace` at 1280 × 780 using its `--smoke-test`
and `--screenshot` options with Segoe UI, then converted from BMP to PNG.
Update screenshots when the corresponding examples change.

The design uses original styles and markup. The clear getting-started paths on
[raylib](https://www.raylib.com/) and visual demonstrations on
[Slint](https://slint.dev/) informed the information hierarchy.


## Project boundaries

This repository owns the public website. Library code, examples, tests and
technical Markdown guides remain in [vectorgl](https://github.com/mahtab04/vectorgl).
Source/header/example links deliberately point there; website metadata and
sitemaps use <https://mahtab04.github.io/vectorgl-website/>.

The initial site was migrated from VectorGL commit
`22353c7` (merged website redesign, PR #31). Original history remains in that
repository. Both projects use the MIT license.

## Validation and deployment

```sh
python scripts/check_site.py
node --check site/app.js
```

Python 3 and Node.js are only needed for validation; serving needs no build step
or npm packages. Only `site/` is published. CI scripts, README and repository
metadata are excluded from the deployment artifact.

Before merging changes, check navigation, API search, copy controls and code tabs
in both themes and at narrow mobile widths. The technical guides and API links
must stay aligned with the library; update examples when its public API changes.
