from doc_quality_scorer.metrics import calculate_readability

def test_calculate_readability_empty():
    stats = calculate_readability("")
    assert stats["word_count"] == 0
    assert stats["sentence_count"] == 0
    assert stats["flesch_kincaid"] == 0.0

def test_calculate_readability_simple():
    text = "The cat sat on the mat. It was a good cat."
    stats = calculate_readability(text)
    assert stats["sentence_count"] == 2
    assert stats["word_count"] == 11
    assert stats["flesch_kincaid"] > 80.0
