# Pasos para ejecutar el proyecto
```
         _nnnn_                      
        dGGGGMMb     ,"""""""""""""".
       @p~qp~~qMb    | Kotlin Rules! |
       M|@||@) M|   _;..............'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
    dZP          qKKb
fZP            SMMb
HZM            MMMM
FqM            MMMM
__| ".        |\dS"qML
|    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
`-'       `--' hjm
```
## 1) Descargar recursos mediante scrapper


```bash
python3 -m venv venv 
source venv/bin/activate


pip install -U pip
pip install -r requirements.txt
pip install playwright
pip install csv
pip install re 

playwright install

declare ruta="./test/recursos"
declare link="https://link.springer.com/search?new-search=true&query=Computational+Thinking&dateFrom=&dateTo=&sortBy=relevance"
python3 ./src/extractors/springer/scrapper.py $link $ruta
```


## 2) Reunir los resultados en un solo archivo

```bash
declare input_dir="./test/recursos"
declare output_file="./test/collection.ris"

bash ./src/logic/unifier.sh $input_dir $output_file
```

## 3) Convertir el compilado .ris a una table csv

Dar los siguientes dos params 
- ../../../test/collection.ris
- ../../../test/collection.csv

```bash
source venv/bin/activate
cd src/logic/ris_to_csv
python3 ris_converter.py
```

## 4) Para visualizar los requerimientos 2 a 5 
#### (excepto el 4 jaja) simplemente abrir la carpeta con el nombre correspodiente. 
