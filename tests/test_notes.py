from trailbinder.core.notes import extract_links_and_tags
def test_parse():
    s = "Есть [[Связь]] и теги #alpha #beta"
    meta = extract_links_and_tags(s)
    assert "Связь" in meta["links"]
    assert "alpha" in meta["tags"] and "beta" in meta["tags"]
