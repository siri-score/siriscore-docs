"""MkDocs hook that emits redirect stubs for moved pages.

Kept as a local hook instead of the mkdocs-redirects plugin so the build
has no third-party plugin dependencies. Add entries to REDIRECTS as
old-path -> new-URL (both relative to the site root).
"""

import os

REDIRECTS = {}

_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Redirecting…</title>
<link rel="canonical" href="{url}">
<meta http-equiv="refresh" content="0; url={url}">
<script>var a=window.location.hash.substr(1);location.href="{url}"+(a?"#"+a:"")</script>
</head>
<body>
<p>This page has moved to <a href="{url}">a new location</a>.</p>
</body>
</html>
"""


def on_post_build(config, **kwargs):
    for old_path, new_url in REDIRECTS.items():
        target = os.path.join(config["site_dir"], old_path)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w", encoding="utf-8") as f:
            f.write(_TEMPLATE.format(url=new_url))
