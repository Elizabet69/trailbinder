import os, re, json
from typing import List, Dict, Optional

ROOT = os.path.dirname(os.path.dirname(__file__))
BASE = os.path.dirname(ROOT)
NOTES_DIR = os.path.join(BASE, "notes")
META_DIR  = os.path.join(BASE, "data", "meta")

RX_LINK = re.compile(r"\[\[([^\[\]]+)\]\]")
RX_TAG  = re.compile(r"(?<!\w)#([a-zA-Z0-9_\-]+)")

def ensure_dirs():
    os.makedirs(NOTES_DIR, exist_ok=True)
    os.makedirs(META_DIR,  exist_ok=True)

def slugify(s: str) -> str:
    import re
    s = s.strip().lower()
    s = re.sub(r"\s+", "-", s)
    s = re.sub(r"[^a-z0-9\-_]+", "", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "note"

def list_notes() -> List[str]:
    ensure_dirs()
    return sorted([f for f in os.listdir(NOTES_DIR) if f.endswith(".md")])

def read_note(filename: str) -> Optional[str]:
    p = os.path.join(NOTES_DIR, filename)
    return open(p, "r", encoding="utf-8").read() if os.path.exists(p) else None

def write_note(title: str, content: str) -> str:
    ensure_dirs()
    fname = slugify(title) + ".md"
    p = os.path.join(NOTES_DIR, fname)
    with open(p, "w", encoding="utf-8") as f:
        f.write(f"# {title}\n\n{content.strip()}\n")
    return p

def extract_links_and_tags(text: str) -> Dict[str, List[str]]:
    return {
        "links": sorted(set(RX_LINK.findall(text or ""))),
        "tags":  sorted(set(RX_TAG.findall(text or ""))),
    }

def build_index() -> str:
    ensure_dirs()
    idx = {}
    for fn in list_notes():
        idx[fn] = extract_links_and_tags(read_note(fn) or "")
    out = os.path.join(META_DIR, "index.json")
    json.dump(idx, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return out

# autosave 2025-11-10T16:54:19.572678+00:00

# autosave 2025-11-19T11:55:45.515261+00:00
# tweak 2025-11-24T12:08:35.915990+00:00
