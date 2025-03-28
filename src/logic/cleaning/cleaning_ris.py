#!/usr/bin/env python3
# EL OBJETIVO DE ESTE SCRIPT ES ELIMINAR LOS .RIS DUPLICADOS QUE PUEDAN EXISTIR
# EN UN DIRECTORIO

import os
import sys
import shutil
import argparse


def extract_doi(file_path):
    """Extract DOI from a .ris file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith('DO  - '):
                    return line.strip()[6:].strip()  # Remove "DO  - " prefix and whitespace
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return None


def filter_ris_files(input_dir, output_dir):
    """Filter .ris files based on DOI to remove duplicates."""
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Keep track of DOIs we've seen
    seen_dois = set()
    copied_count = 0
    skipped_count = 0

    # Process all files in the input directory
    for filename in os.listdir(input_dir):
        if not filename.endswith('.ris'):
            continue

        file_path = os.path.join(input_dir, filename)
        doi = extract_doi(file_path)

        # If file has no DOI or we haven't seen this DOI before
        if doi is not None and doi not in seen_dois:
            seen_dois.add(doi)
            output_path = os.path.join(output_dir, filename)
            shutil.copy2(file_path, output_path)
            copied_count += 1
        else:
            skipped_count += 1

    print(f"Filtered {copied_count} unique DOIs, skipped {skipped_count} duplicates or files without DOI")


def main():
    parser = argparse.ArgumentParser(description='Filter .ris files to remove duplicates based on DOI')
    parser.add_argument('input_dir', help='Directory containing .ris files')
    parser.add_argument('output_dir', help='Directory to store filtered .ris files')

    args = parser.parse_args()

    if not os.path.isdir(args.input_dir):
        print(f"Error: Input directory '{args.input_dir}' does not exist.")
        sys.exit(1)

    filter_ris_files(args.input_dir, args.output_dir)
    print(f"Filtering complete. Files saved to {args.output_dir}")


if __name__ == '__main__':
    main()
