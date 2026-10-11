# PrecodeOS Squarespace manual install

This package is designed for a private Squarespace 7.1 site. It uses one native Code Block per page plus global Custom CSS and Code Injection. It does not publish the site.

## 1. Save the source files locally

Keep these files open while working:

- `precode-global.css`
- `precode-global.js`
- `precode-home.html`
- `precode-gap.html`
- `precode-comparison.html`
- `precode-pattern.html`
- `precode-start.html`

The five HTML files are the public page content. They are derived from the repository README. Do not paste maintainer-only roadmap, task, release, or private planning material into the site.

## 2. Add the global CSS

1. In Squarespace, open **Website → Design → Custom CSS**.
2. Remove only the old PrecodeOS custom CSS, if one exists. Do not remove unrelated site styles.
3. Open `precode-global.css`, copy the entire file, and paste it into Custom CSS.
4. Save the Custom CSS panel.

## 3. Add the global accordion JavaScript

1. Open **Settings → Advanced → Code Injection**.
2. Paste the complete contents of `precode-global.js` into the **Footer** injection area.
3. Wrap it in `<script>` tags:

```html
<script>
// paste the contents of precode-global.js here
</script>
```

4. Save Code Injection.

If your Squarespace plan does not expose Code Injection, paste the same script in a Code Block on each page after its HTML. The script is idempotent, so repeated page loads are safe.

## 4. Prepare each page

For each of these Squarespace pages, open the page editor and remove the existing placeholder/demo sections only after copying any content you need to retain:

| Squarespace page | File to paste |
|---|---|
| Home | `precode-home.html` |
| The Gap | `precode-gap.html` |
| Comparison | `precode-comparison.html` |
| The Precode Pattern | `precode-pattern.html` |
| Start | `precode-start.html` |

For each page:

1. Add a blank section.
2. Add one **Code** block to that section.
3. Open the source file for that page.
4. Copy the entire file, beginning with `<div class="pc-site"` and ending with `</div>`.
5. Paste it into the Code Block editor.
6. Ensure **Display Source Code** is off.
7. Save the Code Block.
8. Save the page.
9. Exit the page editor.

Do not paste the HTML into a Text Block. Do not paste the CSS into a page Code Block if it is already in Custom CSS. Do not add `<html>`, `<head>`, or `<body>` tags.

## 5. Add page metadata

In each page’s **Page Settings → SEO**, use:

| Page | SEO title | Description |
|---|---|---|
| Home | PrecodeOS — Build with AI Without Losing the Plot | PrecodeOS is a human-directed, repo-native operating model for dependable AI-assisted software building. |
| The Gap | The Gap — Why PrecodeOS Exists | Why fast AI-assisted coding drifts, and how PrecodeOS keeps intent, scope, proof, and recovery visible. |
| Comparison | PrecodeOS Compared with AI Coding Approaches | See how PrecodeOS complements vibe coding, coding agents, traditional SDLC, project management, and agent frameworks. |
| The Precode Pattern | The Precode Pattern — From Intent to Proof | Understand the human-directed Precode Flow: Understand, Shape, Decide, Bound, Build, Prove, Review, and Continue. |
| Start | Start with PrecodeOS | Try PrecodeOS from the public repository with the preview setup route and guided documentation. |

Keep **Hide page from search results** enabled until the site is ready to publish. Add a social image later if you have an approved public brand asset.

## 6. Verify before publishing

Perform this sequence on every page:

1. In the editor, confirm the page shows the large left intro column and the right content column.
2. Click each accordion row. Confirm it opens, closes, and exposes readable text.
3. Confirm the navigation links go to the five intended routes.
4. Save, exit, reload the Squarespace editor, and reopen the page.
5. Open the page preview and confirm the page still renders after reload.
6. Test at a narrow mobile viewport. Confirm the two-column layout collapses to one column and the accordion remains usable.
7. Keyboard-test every navigation link and accordion trigger. Confirm focus is visible and Enter/Space opens an accordion.
8. Check that no private maintainer material appears in the rendered page, page title, metadata, or source.
9. Keep the site private. Do not click **Publish Your Site** until all five pages pass.

## 7. Important Squarespace editor constraint

Do not edit these Code Blocks repeatedly while the editor is in a stale or blank preview state. If a Code Block appears to revert:

1. Save the source file locally first.
2. Exit the editor.
3. Reload Squarespace.
4. Reopen the page.
5. Replace the entire Code Block contents using a fresh Code Block rather than appending to existing content.
6. Save, exit, reload, and verify again.

The source files in this folder remain the canonical copy for manual re-entry.
