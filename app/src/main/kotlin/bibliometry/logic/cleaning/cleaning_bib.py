#!/usr/bin/env python3
# This script removes duplicate .bib files based on their DOI
# RECIBE DOS PARAMETROS POR MEDIO DE LINEA DE COMANDOS
# ARG1 -> El directorio donde están los archivos .bib sin filtrar
# ARG2 -> El directorio donde se filtrarán los archivos, es decir, la carpeta sin duplicados.

import os
import sys
import shutil
import argparse
import re
from typing import Optional, Set


def extract_doi(file_path: str) -> Optional[str]:
    """Extract DOI from a .bib file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content: str = file.read()
            # Look for doi field with regex
            doi_match: Optional[re.Match] = re.search(r'doi\s*=\s*{([^}]+)}', content)
            if doi_match:
                doi: str = doi_match.group(1).strip()
                # Remove any 'https://doi.org/' or 'http://doi.org/' prefix
                doi = re.sub(r'^https?://doi\.org/', '', doi)
                return doi
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None


def filter_bib_files(input_dir: str, output_dir: str) -> None:
    """Filter .bib files based on DOI to remove duplicates."""
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Keep track of DOIs we've seen
    seen_dois: Set[str] = set()
    copied_count: int = 0
    skipped_count: int = 0

    # Process all files in the input directory
    for filename in os.listdir(input_dir):
        if not filename.endswith('.bib'):
            continue

        file_path: str = os.path.join(input_dir, filename)
        doi: Optional[str] = extract_doi(file_path)

        # If file has no DOI or we haven't seen this DOI before
        if doi is not None and doi not in seen_dois:
            seen_dois.add(doi)
            output_path: str = os.path.join(output_dir, filename)
            shutil.copy2(file_path, output_path)
            copied_count += 1
        else:
            skipped_count += 1

    print(f"Filtered {copied_count} unique DOIs, skipped {skipped_count} duplicates or files without DOI")


def main() -> None:
    parser = argparse.ArgumentParser(description='Filter .bib files to remove duplicates based on DOI')
    parser.add_argument('input_dir', help='Directory containing .bib files')
    parser.add_argument('output_dir', help='Directory to store filtered .bib files')

    args = parser.parse_args()

    if not os.path.isdir(args.input_dir):
        print(f"Error: Input directory '{args.input_dir}' does not exist.")
        sys.exit(1)

    filter_bib_files(args.input_dir, args.output_dir)
    print(f"Filtering complete. Files saved to {args.output_dir}")


if __name__ == '__main__':
    main()