#!/usr/bin/python3
import re
from pybtex.database import BibliographyData, Entry

def ris_to_bib(ris_file, bib_file):
    with open(ris_file, 'r', encoding='utf-8') as f:
        ris_content = f.readlines()

    entries = []
    entry = {}
    for line in ris_content:
        match = re.match(r'^(\w{2})  - (.*)', line)
        if match:
            key, value = match.groups()
            if key == 'TY':  # Start of a new entry
                if entry:
                    entries.append(entry)
                entry = {'type': value.lower()}
            elif key == 'ER':  # End of entry
                entries.append(entry)
                entry = {}
            else:
                entry.setdefault(key, []).append(value)

    if entry:
        entries.append(entry)

    bib_entries = {}
    for entry in entries:
        if not entry:
            continue

        bib_key = entry.get('DO', ['unknown'])[0]
        bib_type = 'article' if entry.get('TY', [''])[0] == 'JOUR' else 'misc'

        bib_entries[bib_key] = Entry(
            bib_type,
            fields={
                'title': f"{{{entry.get('TI', [''])[0]}}}",
                'author': f"{{{' and '.join(entry.get('AU', []))}}}",
                'journal': f"{{{entry.get('JO', [''])[0]}}}",
                'year': f"{{{entry.get('PY', [''])[0]}}}",
                'volume': f"{{{entry.get('VL', [''])[0]}}}",
                'number': f"{{{entry.get('IS', [''])[0]}}}",
                'pages': f"{{{entry.get('SP', [''])[0]}--{entry.get('EP', [''])[0]}}}",
                'doi': f"{{{entry.get('DO', [''])[0]}}}",
                'url': f"{{{entry.get('UR', [''])[0]}}}",
                'publisher': f"{{{entry.get('PB', [''])[0]}}}",
                'issn': f"{{{entry.get('SN', [''])[0]}}}",
                'keywords': f"{{{', '.join(entry.get('KW', []))}}}",
                'abstract': f"{{{entry.get('AB', [''])[0]}}}"
            }
        )

    bib_data = BibliographyData(entries=bib_entries)
    with open(bib_file, 'w', encoding='utf-8') as f:
        f.write(bib_data.to_string('bibtex'))

# Uso de la función
txt_input = "nombre1.ris"
txt_output = "nombre2.bib"
ris_to_bib(txt_input, txt_output)
