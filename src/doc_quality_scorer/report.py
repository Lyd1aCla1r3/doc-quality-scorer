import json

def _analyze_metrics(structure: dict, readability: dict, fidelity: dict) -> dict:
    analysis = {}
    
    # Readability
    fk = readability.get("flesch_kincaid", 0)
    flagged = readability.get("flagged_sentences", [])
    if fk < 50:
        msg = "Score is penalized due to overly complex sentence structures.\n\n**Action:** Simplify the following flagged sentences:"
        if flagged:
            for s in flagged:
                msg += f"\n> \"{s}\"\n"
        analysis["readability_analysis"] = msg
    elif fk > 80:
        analysis["readability_analysis"] = "Score indicates extremely simple text.\n\n**Action:** Ensure necessary technical depth and precision are not sacrificed."
    else:
        analysis["readability_analysis"] = "Readability is within the optimal range (60-80) for technical documentation."
        
    # Fidelity
    cons = fidelity.get("consistency_score", 0)
    drifting = fidelity.get("drifting_terms", [])
    if cons < 0.10:
        msg = "Score is heavily penalized due to high semantic drift.\n\n**Action:** Unify your terminology. The following terms are used inconsistently across different sections:\n"
        if drifting:
            msg += "\n> `" + "`, `".join(drifting) + "`\n"
        analysis["fidelity_analysis"] = msg
    else:
        analysis["fidelity_analysis"] = "High semantic consistency. Terminology remains cohesive and focused across sections."
        
    # Structure
    if structure.get("headings", 0) == 0:
        analysis["structure_analysis"] = "The document lacks structural hierarchy. Action: Add structured headings (##) to break up walls of text and improve scannability."
    else:
        analysis["structure_analysis"] = "Document is properly partitioned with structural elements."
        
    return analysis

def generate_report(file_path: str, structure: dict, readability: dict, fidelity: dict, score: float, output_format: str = "json") -> str:
    """Formats the calculated metrics into structured quality reports."""
    analysis = _analyze_metrics(structure, readability, fidelity)
    
    data = {
        "file": file_path,
        "composite_score": round(score, 2),
        "structure": structure,
        "readability": {
            "flesch_kincaid": round(readability.get("flesch_kincaid", 0), 2),
            "word_count": readability.get("word_count", 0),
            "sentence_count": readability.get("sentence_count", 0),
            "flagged_sentences": readability.get("flagged_sentences", [])
        },
        "fidelity": {
            "consistency_score": round(fidelity.get("consistency_score", 0), 4),
            "section_count": fidelity.get("section_count", 0),
            "drifting_terms": fidelity.get("drifting_terms", [])
        },
        "analysis": analysis
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

**Analysis**: {analysis['structure_analysis']}

### Readability
- Flesch-Kincaid Reading Ease: {data["readability"]["flesch_kincaid"]}
- Word Count: {data["readability"]["word_count"]}

**Analysis**: {analysis['readability_analysis']}

### Fidelity & Consistency
- Semantic Consistency: {data["fidelity"]["consistency_score"]}

**Analysis**: {analysis['fidelity_analysis']}
"""
