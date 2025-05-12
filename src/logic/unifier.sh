#!/bin/bash
# SCRIPT PARA ESCRIBIR EL CONTENIDO DE LOS ARCHIVOS .RIS DE UNA CARPETA A UN SOLO ARCHIVO DE SALIDA
# Define la shell que se usará para ejecutar el script (Bash)

declare input_dir=$1
declare output_file=$2
# Declara dos variables para almacenar los argumentos de entrada:
# $1: directorio de entrada que contiene los archivos .ris a unificar
# $2: archivo de salida donde se combinarán todos los contenidos

# Verificar si se proporcionaron los argumentos necesarios
if [ -z "$input_dir" ] || [ -z "$output_file" ]; then
    echo "Uso: $0 <directorio_entrada> <archivo_salida>"
    exit 1
fi
# Verifica si se proporcionaron los dos argumentos necesarios
# Si falta alguno, muestra un mensaje de uso y termina el script con código de error 1

# Crear o limpiar el archivo de salida
> "$output_file"
# Crea un archivo vacío o borra el contenido si ya existe
# usando el operador de redirección ">"

# Contador para archivos procesados
contador=0

# Recorrer todos los archivos .ris en el directorio
for file in "$input_dir"/*.ris; do
    # Comprobar si el archivo existe y es un archivo regular
    if [ -f "$file" ]; then
        cont=`cat "$file"`
        echo -e "$cont\n\n" >> "$output_file"
        # Para cada archivo .ris:
        # 1. Lee su contenido y lo guarda en la variable "cont"
        # 2. Añade el contenido al archivo de salida seguido de dos líneas en blanco
        # (usando la redirección de añadido ">>")

        echo "Añadido $(basename "$file") a $output_file"
        # Muestra un mensaje indicando que se ha añadido el archivo al documento unificado
        ((contador++))
    fi
done
# El bucle procesa solo los archivos con extensión .ris del directorio de entrada

echo "Se han unificado $contador archivos .ris en $output_file"
# Muestra un mensaje final indicando que se ha completado la unificación y cuántos archivos se procesaron
