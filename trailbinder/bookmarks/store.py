import os, json
from datetime import datetime
from typing import List, Optional, Dict

BASE = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
BM_DIR = os.path.join(BASE, "bookmarks")

def ensure_dir(): os.makedirs(BM_DIR, exist_ok=True)

def add_bookmark(url: str, title: Optional[str]=None, tags: Optional[List[str]]=None, note: str="") -> str:
    ensure_dir()
    day = datetime.now().strftime("%Y-%m-%d")
    p = os.path.join(BM_DIR, f"{day}.json")
    data: Dict[str, list] = {"bookmarks": []}
    if os.path.exists(p): data = json.load(open(p,"r",encoding="utf-8"))
    data["bookmarks"].append({"ts": datetime.now().isoformat(), "url": url, "title": title or "", "tags": tags or [], "note": note})
    json.dump(data, open(p,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
    return p

# autosave 2025-10-15T14:59:08.230839+00:00
