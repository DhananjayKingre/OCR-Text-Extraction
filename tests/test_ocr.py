from src.text_extraction import extract_target_line

def test_extract_target_line():
    lines = [
        "Normal text",
        "123456789_1_ABC",
        "Other line"
    ]
    assert extract_target_line(lines) == "123456789_1_ABC"
