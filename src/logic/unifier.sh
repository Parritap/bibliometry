#!/bin/bash
# SCRIPT ESCRIBIR TODO EL CONTENIDO DE UNA CARPETA INDICADA POR PARAMETRO A UN ARCHIVO TAMBIEN PASASO POR PAMETRO
# Define la shell que se usará para ejecutar el script (Bash)

declare input_dir=$1
declare output_file=$2
# Declara dos variables para almacenar los argumentos de entrada:
# $1: directorio de entrada que contiene los archivos a unificar
# $2: archivo de salida (otro .bib en blanco de preferencia) donde se combinarán todos los contenidos

# Check if arguments are provided
if [ -z "$input_dir" ] || [ -z "$output_file" ]; then
    echo "Usage: $0 <input_directory> <output_file>"
    exit 1
fi
# Verifica si se proporcionaron los dos argumentos necesarios
# Si falta alguno, muestra un mensaje de uso y termina el script con código de error 1

# Create or clear the output file
> "$output_file"
# Crea un archivo vacío o borra el contenido si ya existe
# usando el operador de redirección ">"

# Loop through all files in the directory
for file in "$input_dir"/*; do
    if [ -f "$file" ]; then
        cont=`cat "$file"`
        echo -e "$cont\n\n" >> "$output_file"
        # Para cada archivo:
        # 1. Lee su contenido y lo guarda en la variable "cont"
        # 2. Añade el contenido al archivo de salida seguido de dos líneas en blanco
        # (usando la redirección de añadido ">>")

        echo "Added $(basename "$file") to $output_file"
        # Muestra un mensaje indicando que se ha añadido el archivo al documento unificado
    fi
done
# El bucle procesa todos los archivos del directorio de entrada

echo "All files have been unified into $output_file"
# Muestra un mensaje final indicando que se ha completado la unificación