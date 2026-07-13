import json

def generate_report(file_path: str, structure: dict, readability: dict, fidelity: dict, score: float, output_format: str = "json") -> str:
    """Formats the calculated metrics into structured quality reports."""
    data = {
        "file": file_path,
        "composite_score": round(score, 2),
        "structure": structure,
        "readability": {
            "flesch_kincaid": round(readability.get("flesch_kincaid", 0), 2),
            "word_count": readability.get("word_count", 0),
            "sentence_count": readability.get("sentence_count", 0)
        },
        "fidelity": {
            "consistency_score": round(fidelity.get("consistency_score", 0), 4),
            "section_count": fidelity.get("section_count", 0)
        }
    }
    
    if output_format == "json":
        return json.dumps(data, indent=2)
    else:
        return f"""# Quality Report: {file_path}

## Overall Score: {data["composite_score"]}/100

### Structure
- Headings: {structure.get("headings", 0)}
- Paragraphs: {structure.get("paragraphs", 0)}
- Code Blocks: {structure.get("code_blocks", 0)}

### Readability
- Flesch-Kincaid Reading Ease: {data["readability"]["flesch_kincaid"]}
- Word Count: {data["readability"]["word_count"]}

### Fidelity & Consistency
- Semantic Consistency: {data["fidelity"]["consistency_score"]}
"""
