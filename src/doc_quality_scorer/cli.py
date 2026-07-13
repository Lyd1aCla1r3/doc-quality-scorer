import argparse
import sys
from pathlib import Path
from doc_quality_scorer.parser import parse_markdown_structure
from doc_quality_scorer.metrics import calculate_readability
from doc_quality_scorer.scorer import calculate_fidelity_score, composite_score
from doc_quality_scorer.report import generate_report

def process_file(file_path: Path, output_format: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}", file=sys.stderr)
        sys.exit(1)
        
    structure = parse_markdown_structure(text)
    readability = calculate_readability(text)
    fidelity = calculate_fidelity_score(text)
    score = composite_score(readability, structure, fidelity)
    
    report = generate_report(str(file_path), structure, readability, fidelity, score, output_format)
    print(report)

def main():
    parser = argparse.ArgumentParser(description="Document Quality Scorer")
    parser.add_argument("file", help="Path to markdown file")
    parser.add_argument("--format", choices=["json", "markdown"], default="json", help="Output format")
    
    args = parser.parse_args()
    
    file_path = Path(args.file)
    if not file_path.exists():
        print(f"Error: File {args.file} not found.", file=sys.stderr)
        sys.exit(1)
        
    process_file(file_path, args.format)

if __name__ == "__main__":
    main()
