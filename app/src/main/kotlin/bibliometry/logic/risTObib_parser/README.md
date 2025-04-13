# Conversor RIS a BibTeX

Este script convierte archivos en formato **RIS** a **BibTeX**, asegurando que todos los valores en la salida estén correctamente formateados y encerrados entre llaves `{}`.

## 📌 Requisitos

- Python 3.x  
- La librería **[pybtex](https://pypi.org/project/pybtex/)**

## 📥 Instalación

1. Clona o descarga este repositorio en tu máquina.  
2. Instala las dependencias ejecutando en la terminal:

   ```bash
   pip install pybtex
   ```

## 🚀 Uso

1. **Ubicación del archivo:**  
   Coloca el archivo RIS (por ejemplo, `ejemplo.ris`) dentro de la misma carpeta que el script.

2. **Configuración de nombres de archivos:**  
   Abre el script y modifica las variables correspondientes para definir el nombre del archivo de entrada y el de salida. Por ejemplo:

   ```python
   txt_input = "ejemplo.ris"  # Archivo RIS de entrada
   txt_output = "referencias.bib"  # Archivo BibTeX que se generará
   ```

3. **Ejecución:**  
   Ejecuta el script en la terminal con:

   ```bash
   python RIStoBIB.py
   ```

   Se generará el archivo BibTeX (por ejemplo, `referencias.bib`) con las entradas correctamente convertidas y formateadas.

## 🔍 Descripción del Script

El script realiza lo siguiente:

- **Lectura del archivo RIS:**  
  - Usa `re` para interpretar el contenido estructurado.
  - Extrae y organiza la información para convertirla a BibTeX.

- **Mapeo de campos:**  
  Convierte los campos RIS a los equivalentes en BibTeX:

  | **Campo RIS**      | **Campo BibTeX** |
  |--------------------|-----------------|
  | AU (Autor)        | author          |
  | TI (Título)       | title           |
  | JO (Revista)      | journal         |
  | PY (Año)         | year            |
  | VL (Volumen)      | volume          |
  | IS (Número)       | number          |
  | SP (Página inicio) - EP (Página fin) | pages   |
  | DO (DOI)          | doi             |
  | UR (URL)          | url             |
  | PB (Editorial)    | publisher       |
  | SN (ISSN)         | issn            |

- **Formato de salida:**  
  Genera un archivo BibTeX con todos los valores encerrados en `{}` para garantizar compatibilidad con gestores de referencias.

## 📌 Ejemplo de Salida

Si el archivo `.ris` contiene:

```
TY  - JOUR
AU  - Gadolin, Christian
AU  - Andersson, Thomas
TI  - Healthcare quality improvement work: a professional employee perspective
JO  - International Journal of Health Care Quality Assurance
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

