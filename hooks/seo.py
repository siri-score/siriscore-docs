"""MkDocs hook that derives per-page SEO meta descriptions.

Material renders <meta name="description"> from page.meta.description and
falls back to site_description otherwise. This hook fills page.meta.description
from the page's first prose paragraph so every page gets a unique snippet
without hand-written frontmatter. Frontmatter `description:` always wins,
and pages with no extractable prose (e.g. HTML-first pages like the landing
page) keep the site-wide description.
"""

import re

# Google truncates snippets around 155-160 characters
_MAX_LEN = 160

# Line starts that aren't prose: headings, raw HTML, admonitions/images,
# tables, lists, icon shortcodes, fences, blockquotes
_SKIP_PREFIXES = ("#", "<", "!", "|", "-", "*", ":", ">", "=")


def _first_paragraph(markdown):
    lines = []
    in_fence = False
    for line in markdown.splitlines():
        stripped = line.strip()
        if stripped.startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not stripped or stripped.startswith(_SKIP_PREFIXES):
            if lines:
                break
            continue
        lines.append(stripped)
    return " ".join(lines)


def _clean(text):
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)  # images
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)  # links -> label
    text = re.sub(r"<[^>]+>", "", text)  # inline HTML
    text = re.sub(r"[*_`]", "", text)  # emphasis / code markers
    return re.sub(r"\s+", " ", text).strip()


def on_page_markdown(markdown, page, config, files):
    if page.meta.get("description"):
        return markdown
    text = _clean(_first_paragraph(markdown))
    if not text:
        return markdown
    if len(text) > _MAX_LEN:
        text = text[:_MAX_LEN].rsplit(" ", 1)[0].rstrip(" ,;:.") + "…"
    page.meta["description"] = text
    return markdown
