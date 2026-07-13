import markdown
from html.parser import HTMLParser

class StructureParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stats = {
            "headings": 0,
            "paragraphs": 0,
            "lists": 0,
            "code_blocks": 0,
            "links": 0
        }

    def handle_starttag(self, tag, attrs):
        if tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            self.stats["headings"] += 1
        elif tag == "p":
            self.stats["paragraphs"] += 1
        elif tag in ["ul", "ol"]:
            self.stats["lists"] += 1
        elif tag == "pre":
            self.stats["code_blocks"] += 1
        elif tag == "a":
            self.stats["links"] += 1

def parse_markdown_structure(text: str) -> dict:
    """Parses markdown text into structural components."""
    html = markdown.markdown(text)
    parser = StructureParser()
    parser.feed(html)
    return parser.stats
