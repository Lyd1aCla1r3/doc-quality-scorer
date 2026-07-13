from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def evaluate_consistency(sections: list[str]) -> tuple[float, list[str]]:
    """Returns average cosine similarity and top drifting terms."""
    if len(sections) <= 1:
        return 1.0, []
        
    vectorizer = TfidfVectorizer(stop_words='english')
    try:
        tfidf_matrix = vectorizer.fit_transform(sections)
    except ValueError:
        return 1.0, []
        
    sim_matrix = cosine_similarity(tfidf_matrix)
    np.fill_diagonal(sim_matrix, np.nan)
    avg_sim = np.nanmean(sim_matrix)
    
    if np.isnan(avg_sim):
        return 1.0, []
        
    # Find terms with highest variance across sections
    feature_names = vectorizer.get_feature_names_out()
    dense_matrix = tfidf_matrix.toarray()
    variances = np.var(dense_matrix, axis=0)
    top_indices = np.argsort(variances)[::-1][:5]
    drifting_terms = [feature_names[i] for i in top_indices if variances[i] > 0]
    
    return float(avg_sim), drifting_terms

def calculate_fidelity_score(text: str) -> dict:
    sections = [p.strip() for p in text.split("\n\n") if len(p.strip()) > 20]
    consistency, drifting_terms = evaluate_consistency(sections)
    return {
        "consistency_score": consistency,
        "section_count": len(sections),
        "drifting_terms": drifting_terms
    }

def composite_score(readability: dict, structure: dict, fidelity: dict) -> float:
    fk = readability.get("flesch_kincaid", 0)
    readability_points = max(0, 100 - min(abs(fk - 65), 50) * 2)
    consistency = fidelity.get("consistency_score", 0.0)
    consistency_points = consistency * 100
    
    return (readability_points * 0.4) + (consistency_points * 0.6)
