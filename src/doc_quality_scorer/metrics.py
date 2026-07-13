import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import re

def ensure_nltk_resources():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt', quiet=True)
    try:
        nltk.data.find('tokenizers/punkt_tab')
    except LookupError:
        nltk.download('punkt_tab', quiet=True)

def count_syllables(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if not word:
        return 0
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count <= 0:
        count = 1
    return count

def calculate_readability(text: str) -> dict:
    """Calculates Flesch-Kincaid Reading Ease and standard counts."""
    ensure_nltk_resources()
    sentences = sent_tokenize(text)
    if not sentences:
        return {"flesch_kincaid": 0.0, "word_count": 0, "sentence_count": 0, "flagged_sentences": []}

    words = [w for w in word_tokenize(text) if re.search(r'\w', w)]
    word_count = len(words)
    sentence_count = len(sentences)
    syllable_count = sum(count_syllables(w) for w in words)

    if word_count == 0 or sentence_count == 0:
        return {"flesch_kincaid": 0.0, "word_count": 0, "sentence_count": 0, "flagged_sentences": []}

    # Flesch-Kincaid Reading Ease
    fk_score = 206.835 - 1.015 * (word_count / sentence_count) - 84.6 * (syllable_count / word_count)
    
    # Flag lowest scoring sentences
    sentence_scores = []
    for s in sentences:
        s_words = [w for w in word_tokenize(s) if re.search(r'\w', w)]
        s_wc = len(s_words)
        if s_wc > 3:
            s_syl = sum(count_syllables(w) for w in s_words)
            s_fk = 206.835 - 1.015 * (s_wc / 1) - 84.6 * (s_syl / s_wc)
            sentence_scores.append((s_fk, s))
            
    sentence_scores.sort(key=lambda x: x[0])
    
    flagged_sentences = []
    for score, s in sentence_scores:
        if score < 40 and len(flagged_sentences) < 3:
            # Clean up markdown hashes and collapse newlines for cleaner output
            clean_s = re.sub(r'#+\s*', '', s).strip()
            clean_s = ' '.join(clean_s.split())
            flagged_sentences.append(clean_s)
    
    return {
        "flesch_kincaid": fk_score,
        "word_count": word_count,
        "sentence_count": sentence_count,
        "flagged_sentences": flagged_sentences
    }
