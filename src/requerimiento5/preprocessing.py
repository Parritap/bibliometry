# src/requerimiento5/preprocessing.py
from typing import List

import nltk
from nltk.corpus import wordnet, stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# --- Verificación y Descarga de Datos NLTK ---
def check_and_download_nltk_data():
    """Verifica si los paquetes necesarios de NLTK están descargados, si no, los descarga."""
    required_packages = ['punkt', 'averaged_perceptron_tagger', 'wordnet', 'omw-1.4', 'stopwords']
    try:
        # Intentar encontrar los paquetes en las rutas conocidas por NLTK
        for package in required_packages:
            nltk.data.find(f'tokenizers/{package}' if package == 'punkt' else
                           f'taggers/{package}' if package == 'averaged_perceptron_tagger' else
                           f'corpora/{package}' if package in ['wordnet', 'omw-1.4', 'stopwords'] else
                           f'{package}') # Ajustar rutas si es necesario para otros tipos
        # print("Datos de NLTK necesarios ya están descargados.")
    except LookupError:
        print("Algunos datos de NLTK no se encontraron. Descargando...")
        for package in required_packages:
            try:
                # Descargar solo si falla la búsqueda individual (más robusto)
                nltk.data.find(f'tokenizers/{package}' if package == 'punkt' else
                               f'taggers/{package}' if package == 'averaged_perceptron_tagger' else
                               f'corpora/{package}' if package in ['wordnet', 'omw-1.4', 'stopwords'] else
                               f'{package}')
            except LookupError:
                print(f"Descargando {package}...")
                nltk.download(package, quiet=True)
        print("Descarga de datos NLTK completada.")

# Ejecutar la verificación al importar el módulo
check_and_download_nltk_data()
# --------------------------------------------

lemmatizer = WordNetLemmatizer()

# Mapeo de etiquetas POS de NLTK a etiquetas que WordNetLemmatizer entiende
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN # Por defecto, tratar como sustantivo

def preprocess_text(text: str, language: str = 'english') -> List[str]:
    """
    Preprocesa un texto para obtener una lista de lemas efectivos
    (sustantivos, verbos, adjetivos lematizados y en minúsculas).

    Args:
        text: El texto del abstract a procesar. Puede ser None o NaN.
        language: Idioma para stopwords ('english', 'spanish', etc.).

    Returns:
        Lista de lemas efectivos. Lista vacía si el texto es None, NaN o vacío.
    """
    # Manejar textos nulos o no string (común en DataFrames)
    if not isinstance(text, str) or not text:
        return []

    # 1. Tokenizar
    tokens = nltk.word_tokenize(text.lower())

    # 2. Eliminar puntuación y números
    tokens = [word for word in tokens if word.isalpha()]

    # 3. Eliminar stopwords
    try:
        stop_words = set(stopwords.words(language))
        tokens = [word for word in tokens if word not in stop_words]
    except IOError:
        # print(f"Advertencia: Stopwords para '{language}' no encontradas. Continuando sin eliminar stopwords.")
        pass # Continuar sin stopwords si no se encuentran

    # 4. Etiquetado POS
    pos_tags = nltk.pos_tag(tokens)

    # 5. Lemmatizar y filtrar por POS (N, V, J - Sustantivo, Verbo, Adjetivo)
    effective_lemmas = []
    for word, tag in pos_tags:
        wnet_pos = get_wordnet_pos(tag)
        # Solo lematizar y añadir si es Sustantivo, Verbo o Adjetivo
        if wnet_pos in [wordnet.NOUN, wordnet.VERB, wordnet.ADJ]:
            lemma = lemmatizer.lemmatize(word, pos=wnet_pos)
            effective_lemmas.append(lemma)

    return effective_lemmas
