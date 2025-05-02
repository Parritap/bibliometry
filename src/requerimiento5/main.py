# src/requerimiento5/main.py
from typing import List, Tuple

import pandas as pd
import os # Para construir rutas de archivo

# Importar las funciones de los nuevos módulos
from preprocessing import preprocess_text
from similarity_metrics import cosine_similarity_effective_lemmas, jaccard_similarity_effective_lemmas

# --- 1. Cargar los datos ---
# Construir la ruta al archivo CSV de forma relativa
def cargar_datos():
    script_dir = os.path.dirname(__file__) # Directorio donde está este script (requerimiento5)
    csv_path = os.path.join(script_dir, '..', 'logic', 'collection.csv') # Ruta a ../logic/collection.csv

    try:
        df = pd.read_csv(csv_path)
        print(f"Datos cargados desde {csv_path}. Total de artículos: {len(df)}")
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {csv_path}")
        print("Asegúrate de que el archivo collection.csv exista en la carpeta 'logic'.")
        exit() # Salir si no se pueden cargar los datos


# la tupla consiste de (doi, abstract) #
# Retorna una lista de tuplas (doi, similitud)
def compare_all_arts_tech_one(
        art: Tuple[str, List[str]], list_simil: List[Tuple[str, List[str]]]
) -> List[Tuple[str, float]]:
    result = []
    for j in range(0, len(list_simil)):
        # Comparar los abstracts
        cos_sim_ij = cosine_similarity_effective_lemmas(art[1], list_simil[j][1])
        result.append((list_simil[j][0], cos_sim_ij))
    return result


# la tupla consiste de (doi, abstract) #
# Retorna una lista de tuplas (doi, similitud)
def compare_all_arts_tech_two(
        art: Tuple[str, List[str]], list_simil: List[Tuple[str, List[str]]]
) -> List[Tuple[str, float]]:
    result = []
    for j in range(0, len(list_simil)):
        # Comparar los abstracts
        jac_sim_ij = jaccard_similarity_effective_lemmas(art[1], list_simil[j][1])
        result.append((list_simil[j][0], jac_sim_ij))
    return result


def create_tupla(index: int, df) -> Tuple[str, List[str]]:
    """
    Crea una tupla con el índice, DOI y abstract.
    """
    abstract1_text = df.loc[index, 'Abstract']
    lemmas1 = preprocess_text(abstract1_text, language='english')
    return (df.loc[index, 'DOI'], lemmas1)

def create_list_tupla(index: int, df) -> List[Tuple[str, List[str]]]:
    """
    Crea una lista de tuplas con el índice, DOI y abstract.
    """
    list_tupla = []
    for i in range(index, len(df)):
        list_tupla.append(create_tupla(i, df))
    return list_tupla

def init():
    print("--- Ejecutando Requerimiento 5: Cálculo de Similitud entre Abstracts ---")

    # Cargar los datos
    df = cargar_datos()

    # Create el primer abstract con los demás
    primer_tupla = create_tupla(0, df)

    list_tupla = create_list_tupla(1, df)


    # Comparar el primer abstract con los demás
    result1 = compare_all_arts_tech_one(primer_tupla, list_tupla)
    #result2 = compare_all_arts_tech_two(primer_tupla, list_tupla)

    df_results = pd.DataFrame(result1, columns=["DOI", "Cosine Similarity"])

