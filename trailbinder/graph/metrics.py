from typing import Dict, List, Tuple

def out_degree(g: Dict[str, List[str]]) -> Dict[str, int]:
    return {k: len(v) for k, v in g.items()}

def in_degree(g: Dict[str, List[str]]) -> Dict[str, int]:
    inc = {k: 0 for k in g}
    for vs in g.values():
        for t in vs:
            if t in inc: inc[t] += 1
    return inc

def top_by_out(g: Dict[str, List[str]], n: int = 5) -> List[Tuple[str, int]]:
    return sorted(((k, len(v)) for k, v in g.items()), key=lambda x: -x[1])[:n]

# autosave 2025-10-06T11:33:13.061825+00:00

# autosave 2025-11-10T18:25:32.823426+00:00

# autosave 2025-12-01T17:22:56.828253+00:00

# autosave 2025-12-08T17:57:41.118193+00:00

# autosave 2025-12-15T19:48:18.964014+00:00

# autosave 2026-01-09T21:13:26.626720+00:00
