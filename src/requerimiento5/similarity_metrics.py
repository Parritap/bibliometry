# src/requerimiento5/similarity_metrics.py

import math
from collections import Counter
from typing import List


# Hamed Hassanzadeh, Diego Mollá, Tudor Groza, Anthony Nguyen and Jane Hunter. 2015.
# Similarity Metrics for Clustering PubMed Abstracts for Evidence Based Medicine.
# In Proceedings of Australasian Language Technology Association Workshop, pages 48-56.
#

def cosine_similarity_effective_lemmas(abstract1_lemmas: List[str], abstract2_lemmas: List[str]) -> float:
    """
    Calcula la similitud coseno entre dos listas de lemas efectivos (palabras lematizadas).
    Basado en la descripción de "Cosine similarity of effective lemmas" en el paper.

    Args:
        abstract1_lemmas: Lista de lemas efectivos del primer abstract.
        abstract2_lemmas: Lista de lemas efectivos del segundo abstract.

    Returns:
        El valor de similitud coseno (entre 0 y 1).
    """
    # Manejar listas vacías
    if not abstract1_lemmas or not abstract2_lemmas:
        return 0.0

    # Contar la frecuencia de cada lema en cada abstract
    vec1 = Counter(abstract1_lemmas)
    vec2 = Counter(abstract2_lemmas)

    # Encontrar la intersección de lemas (palabras presentes en ambos)
    intersection = set(vec1.keys()) & set(vec2.keys())

    # Calcular el producto punto
    numerator = sum(vec1[lemma] * vec2[lemma] for lemma in intersection)

    # Calcular las magnitudes (normas euclidianas)
    sum1 = sum(vec1[lemma]**2 for lemma in vec1.keys())
    sum2 = sum(vec2[lemma]**2 for lemma in vec2.keys())
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0 # Evitar división por cero (aunque ya cubierto por el chequeo inicial)
    else:
        return float(numerator) / denominator

# Hamed Hassanzadeh, Diego Mollá, Tudor Groza, Anthony Nguyen and Jane Hunter. 2015.
# Similarity Metrics for Clustering PubMed Abstracts for Evidence Based Medicine.
# In Proceedings of Australasian Language Technology Association Workshop, pages 48-56.
#

def jaccard_similarity_effective_lemmas(abstract1_lemmas: List[str], abstract2_lemmas: List[str]) -> float:
    """
    Calcula la similitud de Jaccard entre dos conjuntos de lemas efectivos.
    Basado en la descripción de "Jaccard similarity of sets of effective lemmas" en el paper.

    Args:
        abstract1_lemmas: Lista de lemas efectivos del primer abstract.
        abstract2_lemmas: Lista de lemas efectivos del segundo abstract.

    Returns:
        El valor de similitud de Jaccard (entre 0 y 1).
    """
    # Manejar listas vacías
    if not abstract1_lemmas and not abstract2_lemmas:
        return 1.0 # Dos conjuntos vacíos son idénticos por definición Jaccard
    if not abstract1_lemmas or not abstract2_lemmas:
        return 0.0 # Si uno está vacío y el otro no, la similitud es 0

    # Convertir las listas a conjuntos para obtener lemas únicos
    set1 = set(abstract1_lemmas)
    set2 = set(abstract2_lemmas)

    # Calcular la intersección y la unión de los conjuntos
    intersection = set1.intersection(set2)
    union = set1.union(set2)

    # El denominador (unión) no será cero por los chequeos iniciales
    return float(len(intersection)) / len(union)