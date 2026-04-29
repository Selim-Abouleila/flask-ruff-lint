from app.app import format_item

def test_format_item_normal():
    assert format_item("hello") == "Hello"

def test_format_item_with_spaces():
    assert format_item("   world   ") == "World"

def test_format_item_empty():
    assert format_item("") == ""

def test_format_item_none():
    assert format_item(None) == ""
