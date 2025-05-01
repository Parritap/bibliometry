def word_level_similarity(A: str, B: str) -> float:
    # code
    return 0


def word_lemma_similarity(A: str, B: str) -> float:
    # code
    return 0


def set_floatersection_of_effective_lemmas(A: str, B: str) -> float:
    #
    return 0


# la tupla consiste de (doi, abstract) #
# Retorna una lista de tuplas (doi, similitud)
def compare_all_arts_tech_one(
    art: tuple[str, str], list_simil: list[tuple[str, str]]
) -> list[tuple[str, float]]:
    return [("10.01202010120", 0.8), ("10.01202010120", 0.1), ("10.01202010120", 0.3)]


# la tupla consiste de (doi, abstract) #
# Retorna una lista de tuplas (doi, similitud)
def compare_all_arts_tech_two(
    art: tuple[str, str], list_simil: list[tuple[str, str]]
) -> list[tuple[str, float]]:
    return [("10.01202010120", 0.8), ("10.01202010120", 0.1), ("10.01202010120", 0.3)]
