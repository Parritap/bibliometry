"""
Utilidad para convertir archivos BibTeX (.bib) a formato CSV.

Este script permite transformar colecciones bibliográficas en formato BibTeX
a archivos CSV estructurados, facilitando su análisis en hojas de cálculo
u otras herramientas de procesamiento de datos.
"""
import bibtexparser
from bibtexparser.bparser import BibTexParser
import csv

def bib_to_csv(bib_file_path, csv_file_path):
    """
    Convierte un archivo BibTeX (.bib) a formato CSV.
    
    Args:
        bib_file_path (str): Ruta al archivo BibTeX de entrada.
        csv_file_path (str): Ruta donde se guardará el archivo CSV resultante.
    
    El archivo CSV resultante contendrá todas las entradas del archivo BibTeX,
    con una columna para cada campo presente en cualquiera de las entradas.
    """
    # Leer el archivo .bib
    with open(bib_file_path, 'r', encoding='utf-8') as bib_file:
        parser = BibTexParser(common_strings=True)
        bib_database = bibtexparser.load(bib_file, parser=parser)

    # Extraer todos los posibles nombres de campos de las entradas
    all_fields = set()
    for entry in bib_database.entries:
        all_fields.update(entry.keys())
    all_fields = sorted(all_fields)  # Ordenar campos alfabéticamente

    # Escribir en archivo CSV
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=all_fields)
        writer.writeheader()
        for entry in bib_database.entries:
            writer.writerow(entry)

if __name__ == "__main__":
    bib_file_path = "../../resources/collection.bib"  # Reemplazar con la ruta de tu archivo .bib de entrada
    csv_file_path = "../../resources/collection.csv"  # Reemplazar con la ruta deseada para el CSV de salida
    bib_to_csv(bib_file_path, csv_file_path)
