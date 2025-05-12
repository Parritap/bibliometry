#!/bin/bash

#Script para instalar dependencias y crear ambiente virtual

#Esten seguros que están ejecutando esto en la raiz del proyecto para que allí mismo se cree el ambiente virtual.
python3 -m venv venv 


# Activar el ambiente virtual
source venv/bin/activate

#Instalar las dependencias
pip install -U pip
pip install -r requirements.txt
pip install playwright

#instala el navegador chromium para que  playwright pueda funcionar 
playwright install

#USO DEL SCRIPT 
# Copiar link donde se hace la busqueda de los articulos en la pagina de springer
# Escoger la ruta donde se va a descargar el archivo, en nuestro caso será ../../../resources/springer


declare link=$1
declare ruta=$2
python3 scrapper.py $link $ruta
