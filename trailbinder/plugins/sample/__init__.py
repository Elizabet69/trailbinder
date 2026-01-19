import os, json
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
BASE = os.path.dirname(ROOT)
NOTES = os.path.join(BASE, "notes")
META  = os.path.join(BASE, "data", "meta")

def run():
    p = os.path.join(META, "index.json")
    if not os.path.exists(p): return False, "index.json not found"
    idx = json.load(open(p, "r", encoding="utf-8"))
    # добавим счётчик символов для каждой заметки
    for fn in list(idx.keys()):
        fp = os.path.join(NOTES, fn)
        if os.path.exists(fp):
            txt = open(fp, "r", encoding="utf-8").read()
            idx[fn]["chars"] = len(txt)
    json.dump(idx, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return True, "sample plugin updated 'chars'"

# autosave 2025-10-10T11:19:28.026908+00:00

# autosave 2025-10-13T18:07:26.570215+00:00

# autosave 2025-11-17T12:34:12.350215+00:00

# autosave 2025-12-01T21:26:50.438455+00:00

# autosave 2026-01-19T17:30:16.876256+00:00
