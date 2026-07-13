from doc_quality_scorer.parser import parse_markdown_structure

def test_parse_headings():
    text = "# Heading 1\n## Heading 2\n### Heading 3"
    stats = parse_markdown_structure(text)
    assert stats["headings"] == 3

def test_parse_paragraphs():
    text = "Paragraph 1\n\nParagraph 2\n\nParagraph 3"
    stats = parse_markdown_structure(text)
    assert stats["paragraphs"] == 3

def test_parse_lists():
    text = "- Item 1\n- Item 2\n\nSome text.\n\n1. First\n2. Second"
    stats = parse_markdown_structure(text)
    assert stats["lists"] == 2

def test_parse_links():
    text = "[Link 1](http://example.com) and [Link 2](http://example.org)"
    stats = parse_markdown_structure(text)
    assert stats["links"] == 2
