# Conversor RIS a BibTeX

Este script convierte archivos en formato RIS a formato BibTeX, extrayendo y ordenando campos relevantes (autores, título, revista, año, volumen, número, DOI, URL, editorial, ISSN y páginas).

## Requisitos

- Python 3.x  
- La librería [rispy](https://pypi.org/project/rispy/)

## Instalación
 
1. Instala las dependencias ejecutando en la terminal:  
   pip install rispy

## Uso

1. **Ubicación del archivo:**  
   Coloca el archivo RIS (por ejemplo, ejemplo.ris) dentro de la misma carpeta que el script.

2. **Configuración de nombres de archivos:**  
   Abre el script y modifica las variables correspondientes para definir el nombre del archivo de entrada y el de salida. Por ejemplo:  
   - input_ris = "ejemplo.ris" (archivo RIS de entrada)  
   - output_bib = "referencias_final.bib" (archivo BibTeX que se generará)

3. **Ejecución:**  
   Ejecuta el script en la terminal con:  
   python convertir_ris_a_bib.py  
   Se generará el archivo BibTeX (por ejemplo, referencias_final.bib) con las entradas convertidas.

## Descripción del Script

El script realiza lo siguiente:

- **Lectura del archivo RIS:**  
  Lee el archivo y extrae su contenido de forma estructurada (usando rispy) y en bruto para obtener información complementaria.

- **Extracción y mapeo de campos:**  
  Se mapean los campos del RIS a las claves correspondientes en BibTeX, en el siguiente orden:
  - authors → author  
  - title → title  
  - secondary_title → journal  
  - year → year  
  - volume → volume  
  - issue (o la etiqueta IS) → number  
  - doi → doi  
  - url → url (si no se encuentra, se genera a partir del DOI)  
  - publisher → publisher  
  - issn → issn  
  - start_page y end_page → pages

- **Formato de salida:**  
  Se genera una entrada BibTeX ordenada y sin la coma final extra. Por ejemplo, la salida quedaría así:

@article{10.1108/IJHCQA-02-2016-0013,  
  author = {Gadolin, Christian and Andersson, Thomas},  
  title = {Healthcare quality improvement work: a professional employee perspective},  
  journal = {International Journal of Health Care Quality Assurance},  
  year = {2017},  
  volume = {30},  
  number = {5},  
  doi = {10.1108/IJHCQA-02-2016-0013},  
  url = {https://doi.org/10.1108/IJHCQA-02-2016-0013},  
  publisher = {Emerald Publishing Limited},  
  issn = {0952-6862},  
  pages = {410--423}  
}