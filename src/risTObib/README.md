
# Conversor RIS a BibTeX

Este script convierte archivos en formato **RIS** a **BibTeX**, extrayendo y organizando campos clave como autores, título, revista, año, volumen, número, DOI, URL, editorial, ISSN y páginas.

## 📌 Requisitos

- Python 3.x  
- La librería **[rispy](https://pypi.org/project/rispy/)**

## 📥 Instalación

1. Clona o descarga este repositorio en tu máquina.  
2. Instala las dependencias ejecutando en la terminal:

   ```bash
   pip install rispy
   ```

## 🚀 Uso

1. **Ubicación del archivo:**  
   Coloca el archivo RIS (por ejemplo, `ejemplo.ris`) dentro de la misma carpeta que el script.

2. **Configuración de nombres de archivos:**  
   Abre el script y modifica las variables correspondientes para definir el nombre del archivo de entrada y el de salida. Por ejemplo:

   ```python
   input_ris = "ejemplo.ris"  # Archivo RIS de entrada
   output_bib = "referencias_final.bib"  # Archivo BibTeX que se generará
   ```

3. **Ejecución:**  
   Ejecuta el script en la terminal con:

   ```bash
   python convertir_ris_a_bib.py
   ```

   Se generará el archivo BibTeX (por ejemplo, `referencias_final.bib`) con las entradas convertidas.

## 🔍 Descripción del Script

El script realiza lo siguiente:

- **Lectura del archivo RIS:**  
  - Usa `rispy` para interpretar el contenido estructurado.
  - Extrae información complementaria para mejorar el formato.

- **Mapeo de campos:**  
  Convierte los campos RIS a los equivalentes en BibTeX:

  | **Campo RIS**      | **Campo BibTeX** |
  |--------------------|-----------------|
  | authors           | author          |
  | title            | title           |
  | secondary_title  | journal         |
  | year             | year            |
  | volume           | volume          |
  | issue (IS)       | number          |
  | doi              | doi             |
  | url              | url             |
  | publisher        | publisher       |
  | issn             | issn            |
  | start_page - end_page | pages   |

- **Formato de salida:**  
  Genera un archivo BibTeX limpio y estructurado correctamente.

## 📌 Ejemplo de Salida

Si el archivo `.ris` contiene:

```
TY  - JOUR
AU  - Gadolin, Christian
AU  - Andersson, Thomas
TI  - Healthcare quality improvement work: a professional employee perspective
T2  - International Journal of Health Care Quality Assurance
PY  - 2017
VL  - 30
IS  - 5
DO  - 10.1108/IJHCQA-02-2016-0013
UR  - https://doi.org/10.1108/IJHCQA-02-2016-0013
PB  - Emerald Publishing Limited
SN  - 0952-6862
SP  - 410
EP  - 423
ER  -
```

El archivo `.bib` generado será:

```bibtex
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
```