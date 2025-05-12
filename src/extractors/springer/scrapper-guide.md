# Explicación de Scrapper.py

Este script es un web scraper construido con Playwright que extrae y descarga automáticamente archivos de citación de artículos de investigación de Springer.

## Resumen

El script automatiza el proceso de:
1. Navegar a una página de resultados de búsqueda de Springer
2. Iterar a través de cada artículo en la página
3. Hacer clic en cada artículo para acceder a su página de detalles
4. Descargar el archivo de citación para cada artículo
5. Navegar de vuelta a la página de resultados
6. Moverse a la siguiente página de resultados
7. Repetir hasta que todas las páginas sean procesadas

## Funcionalidad Detallada

### Interfaz de Línea de Comandos
- Toma dos argumentos:
  - La URL de los resultados de búsqueda de Springer
  - La ruta donde los archivos de citación deben ser guardados

### Función Principal: `download_files(link, download_path)`
- Crea el directorio de descarga si no existe
- Inicializa Playwright con un navegador visible (headless=False)
- Abre la URL de Springer proporcionada

### Bucle de Navegación de Página
1. Espera 5 segundos para que la página inicial se cargue
2. Para cada página de resultados de búsqueda:
   - Espera a que la lista de resultados aparezca (selector: "ol.u-list-reset")
   - Procesa hasta 20 artículos por página (el número estándar en Springer)

### Bucle de Procesamiento de Artículos
Para cada artículo (1-20) en la página actual:
1. Encuentra el enlace del artículo usando un atributo data-track-context con el contador actual
2. Hace clic en el enlace para abrir la página de detalles del artículo
3. Espera a que la sección de información bibliográfica se cargue
4. Localiza el botón de descarga de la citación
5. Configura un manejador de descarga para capturar el archivo
6. Hace clic en el botón de descarga y guarda el archivo con su nombre de archivo sugerido
7. Navega de vuelta a la página de resultados de búsqueda

### Paginación
Después de procesar todos los artículos en una página:
1. Incrementa el contador de página
2. Busca el botón de "siguiente página"
3. Si lo encuentra, hace clic en él y continúa el procesamiento
4. Si no lo encuentra, termina el proceso de scraping

### Manejo de Errores
- Incluye comprobaciones para elementos faltantes (enlaces de artículos, botones de descarga)
- Imprime mensajes de advertencia cuando los elementos no son encontrados
- Continúa al siguiente artículo/página cuando es posible

## Detalles Técnicos
- Usa la API síncrona de Playwright para la automatización del navegador
- Implementa esperas explícitas para elementos y cargas de página
- Maneja las descargas de archivos a través de la API de descarga de Playwright
- Mantiene el estado a través de las navegaciones de página
- Proporciona salida de consola para rastrear el progreso

El script está diseñado para la descarga por lotes de archivos de citación de artículos de investigación de Springer para fines académicos o de investigación.
