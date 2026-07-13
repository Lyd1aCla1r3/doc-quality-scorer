from doc_quality_scorer.scorer import calculate_fidelity_score, composite_score

def test_fidelity_score_single_section():
    text = "This is a single section.\nIt has some text."
    stats = calculate_fidelity_score(text)
    assert stats["consistency_score"] == 1.0

def test_fidelity_score_consistent_sections():
    text = "The machine learning model is good. The machine learning model is effective.\n\nThe machine learning model is very good. The machine learning model is effective."
    stats = calculate_fidelity_score(text)
    assert stats["consistency_score"] > 0.5
    assert stats["section_count"] == 2

def test_composite_score():
    readability = {"flesch_kincaid": 65.0} # Perfect reading ease target
    structure = {}
    fidelity = {"consistency_score": 1.0} # Perfect consistency
    
    score = composite_score(readability, structure, fidelity)
    assert score == 100.0
