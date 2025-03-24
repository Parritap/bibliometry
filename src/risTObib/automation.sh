#!/bin/bash

#El proposito de este script es convertir MULTIPLES archivos .ris a .bib de manera automática
#El script toma como argumentos la ruta de la carpeta donde están los archivos .ris
#y la ruta de la carpeta donde se guardarán los archivos .bib convertidos.
#El script usa el script RIStoBIB.py para hacer la conversión.

declare inp=$1 #Debe ser la ruta absoluta del lugar donde están los archivos .ris
declare out=$2 #Debe ser la ruta abosluta del lugar donde deberán estar los nuevos archibos .bib

#Usa el Script the python por cada archivo dentro de la carpeta
#especificada en los argumentos, i.e $inp.
for file in "$inp"/*; do
      if [ -f "$file" ]; then
          python3 ./RIStoBIB.py "$file" "$out/$(basename "$file").bib"
          echo  "$(basename file) converted!"
      fi
done

echo "Script finished"
return 0




