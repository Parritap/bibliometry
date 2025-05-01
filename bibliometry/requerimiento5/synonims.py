import nltk
from nltk.corpus import wordnet

# Download required resources (first time only)
nltk.download('wordnet')

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return list(set(synonyms))  # Remove duplicates
