import os, json, re
from typing import Dict, List

ROOT = os.path.dirname(os.path.dirname(__file__))
BASE = os.path.dirname(ROOT)
META_DIR = os.path.join(BASE, "data", "meta")

def slugify(s: str) -> str:
    s = re.sub(r"\s+", "-", s.strip().lower())
    s = re.sub(r"[^a-z0-9\-_]+", "", s)
    return s

def load_index() -> Dict[str, dict]:
    p = os.path.join(META_DIR, "index.json")
    return json.load(open(p, "r", encoding="utf-8")) if os.path.exists(p) else {}

def build_graph() -> Dict[str, List[str]]:
    idx = load_index()
    title2file = {slugify(fn.rsplit(".",1)[0]): fn for fn in idx.keys()}
    g: Dict[str, List[str]] = {fn: [] for fn in idx.keys()}
    for fn, meta in idx.items():
        for link in meta.get("links", []):
            target = title2file.get(slugify(link))
            if target and target != fn and target in g:
                g[fn].append(target)
    return g

# autosave 2025-10-06T11:00:14.934074+00:00

# autosave 2025-10-24T12:53:19.850695+00:00
# tweak 2025-11-12T18:19:51.378038+00:00
# tweak 2025-11-28T19:09:41.492229+00:00

# autosave 2025-12-05T19:33:32.042311+00:00

# autosave 2025-12-12T11:50:15.015191+00:00

# autosave 2026-01-02T10:53:06.888140+00:00

# autosave 2026-01-07T15:34:59.108066+00:00

# autosave 2026-01-16T20:14:24.836922+00:00

# autosave 2026-02-16T20:02:23.259454+00:00
