from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def evaluate_consistency(sections: list[str]) -> float:
    """Returns average cosine similarity across sections. Higher is more consistent."""
    if len(sections) <= 1:
        return 1.0
        
    vectorizer = TfidfVectorizer(stop_words='english')
    try:
        tfidf_matrix = vectorizer.fit_transform(sections)
    except ValueError:
        return 1.0
        
    sim_matrix = cosine_similarity(tfidf_matrix)
    np.fill_diagonal(sim_matrix, np.nan)
    avg_sim = np.nanmean(sim_matrix)
    
    if np.isnan(avg_sim):
        return 1.0
    return float(avg_sim)

def calculate_fidelity_score(text: str) -> dict:
    sections = [p.strip() for p in text.split("\n\n") if len(p.strip()) > 20]
    consistency = evaluate_consistency(sections)
    return {
        "consistency_score": consistency,
        "section_count": len(sections)
    }

def composite_score(readability: dict, structure: dict, fidelity: dict) -> float:
    fk = readability.get("flesch_kincaid", 0)
    readability_points = max(0, 100 - min(abs(fk - 65), 50) * 2)
    consistency = fidelity.get("consistency_score", 0.0)
    consistency_points = consistency * 100
    
    return (readability_points * 0.4) + (consistency_points * 0.6)
