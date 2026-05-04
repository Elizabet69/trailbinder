import os, json
from ..graph.build import build_graph, load_index

ROOT = os.path.dirname(os.path.dirname(__file__))
BASE = os.path.dirname(ROOT)
REPORTS_DIR = os.path.join(BASE, "reports")

def export_all_to_json() -> str:
    os.makedirs(REPORTS_DIR, exist_ok=True)
    out = {"index": load_index(), "graph": build_graph()}
    p = os.path.join(REPORTS_DIR, "export.json")
    json.dump(out, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    return p
# tweak 2025-10-27T21:33:36.482531+00:00

# autosave 2025-10-29T19:33:38.376264+00:00

# autosave 2025-10-31T15:27:40.549709+00:00

# autosave 2026-01-26T14:25:57.001599+00:00

# autosave 2026-02-13T19:36:39.666968+00:00

# autosave 2026-03-11T11:02:21.214452+00:00

# autosave 2026-04-01T14:17:09.343890+00:00
# tweak 2026-05-04T19:11:46.973196+00:00
