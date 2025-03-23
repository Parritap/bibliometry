#!/usr/bin/python3
import re
import sys
import rispy

def extract_issue_for_entry(doi, raw_entries):
    """
    Busca en los bloques de texto del RIS el campo IS (issue) para el DOI dado.
    """
    for raw in raw_entries:
        if doi in raw:
            match = re.search(r'^IS\s+-\s+(.*)$', raw, re.MULTILINE)
            if match:
                return match.group(1).strip()
    return None


def convert_ris_to_bib(ris_file, bib_file):
    """Convierte un archivo .ris a .bib en el orden deseado e incluyendo URL y número (issue)."""
    # Leer el contenido bruto del archivo RIS y separar en bloques (cada entrada termina con 'ER  -')
    with open(ris_file, "r", encoding="utf-8") as f:
        raw_content = f.read()
    raw_entries = raw_content.strip().split("ER  -")

    # Cargar las entradas con rispy
    with open(ris_file, "r", encoding="utf-8") as f:
        entries = rispy.load(f)

    with open(bib_file, "w", encoding="utf-8") as f:
        for entry in entries:
            # Usar DOI si está disponible, o el título, como identificador
            doi = entry.get('doi', None)
            entry_id = doi or entry.get('title', 'unknown')
            entry_id = entry_id.replace(" ", "_").replace(",", "")

            bib_entry = f"@article{{{entry_id},\n"

            # Definir el orden deseado de campos:
            # (clave en rispy, clave en BibTeX)
            ordered_fields = [
                ("authors", "author"),
                ("title", "title"),
                ("secondary_title", "journal"),
                ("year", "year"),
                ("volume", "volume"),
                # "issue" se maneja aparte para el número
                ("doi", "doi"),
                ("url", "url"),
                ("publisher", "publisher"),
                ("issn", "issn")
            ]

            # Recorrer los campos en orden
            for ris_key, bib_key in ordered_fields:
                if ris_key in entry:
                    value = entry[ris_key]
                    if isinstance(value, list):
                        value = " and ".join(value)
                    bib_entry += f"  {bib_key} = {{{value}}},\n"
                else:
                    # Para el campo URL: si no se encuentra y hay DOI, lo generamos
                    if bib_key == "url" and doi:
                        generated_url = f"https://doi.org/{doi}"
                        bib_entry += f"  url = {{{generated_url}}},\n"

            # Manejar el campo "number" (issue)
            issue_value = entry.get("issue")
            if not issue_value and doi:
                issue_value = extract_issue_for_entry(doi, raw_entries)
            if issue_value:
                bib_entry += f"  number = {{{issue_value}}},\n"

            # Manejar las páginas usando 'start_page' y 'end_page'
            start_page = entry.get("start_page", "")
            end_page = entry.get("end_page", "")
            if start_page and end_page:
                bib_entry += f"  pages = {{{start_page}--{end_page}}},\n"
            elif start_page:
                bib_entry += f"  pages = {{{start_page}}},\n"

            # Eliminar la coma final y cerrar la entrada
            bib_entry = bib_entry.rstrip(",\n") + "\n"
            bib_entry += "}\n\n"
            f.write(bib_entry)

    print(f"✅ Conversión completada. Archivo generado: {bib_file}")





#El siguiente bloque hace posible la ejecución mediante la linea de comandos.
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 script.py [ruta de .ris] [ruta the output.bib]")
        sys.exit(1)

    # Get the two arguments
    input_path = sys.argv[1]
    output_path = sys.argv[2]
    convert_ris_to_bib(input_path, output_path)


