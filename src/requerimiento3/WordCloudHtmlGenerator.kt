
package requerimiento3

// Necesitarás la librería org.json. Si usas Gradle, añade:
// implementation("org.json:json:20231013") // O la versión más reciente
import org.json.JSONArray
import org.json.JSONObject

object WordCloudHtmlGenerator {

    /**
     * Genera el contenido HTML para mostrar una nube de palabras.
     *
     * @param wordFrequencies Un mapa donde la clave es la palabra (String) y el valor es su frecuencia (Int).
     * @param canvasId El ID que se usará para el elemento div donde se dibujará la nube.
     * @param wordCloudJsPath La ruta al archivo wordcloud2.js. Puede ser una ruta local relativa
     * (ej. "./wordcloud2.js") si el JS está junto al HTML, una ruta absoluta, o una URL.
     * @return Una cadena de texto con el contenido HTML completo.
     */
    fun generateWordCloudHtml(
        wordFrequencies: Map<String, Int>,
        canvasId: String = "wordCloudCanvas", // ID por defecto para el div
        wordCloudJsPath: String = "./wordcloud2.js" // Ruta por defecto al script
    ): String {
        // Convertir el mapa de frecuencias de Kotlin a un formato que wordcloud2.js espera:
        // una lista de listas, donde cada sublista es [palabra, frecuencia].
        // Ejemplo: [ ["palabra1", 10], ["palabra2", 8], ... ]
        val dataForJs = JSONArray()
        wordFrequencies.forEach { (word, freq) ->
            if (freq > 0) { // Solo incluimos palabras que aparecieron al menos una vez
                val item = JSONArray()
                item.put(word) // La palabra
                item.put(freq) // Su frecuencia
                dataForJs.put(item)
            }
        }

        // Opciones para la librería wordcloud2.js.
        // Puedes encontrar más opciones en la documentación de wordcloud2.js:
        // https://github.com/timdream/wordcloud2.js/blob/master/API.md
        val options = JSONObject()
        options.put("list", dataForJs) // Los datos de palabras y frecuencias
        options.put("gridSize", 12)    // Espacio entre palabras en la cuadrícula, ajusta según veas
        options.put("weightFactor", 6) // Multiplicador para el tamaño de la fuente basado en la frecuencia
        options.put("fontFamily", "Arial, sans-serif") // Familia de fuentes
        options.put("minSize", 8)      // Tamaño mínimo de la fuente en px (0 para usar gridSize/2)
        options.put("color", "random-dark") // Puedes usar 'random-light', colores específicos, o una función
        options.put("backgroundColor", "#FFFFFF") // Color de fondo del canvas (blanco)
        // options.put("rotateRatio", 0.5) // Proporción de palabras que se rotarán (0 a 1)
        // options.put("shape", "circle") // Forma de la nube: 'circle', 'cardioid', 'diamond', 'triangle-forward', etc.

        // Plantilla HTML
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Nube de Palabras</title>
            <script src="$wordCloudJsPath"></script>
            <style>
                body { 
                    margin: 0; 
                    display: flex; 
                    justify-content: center; 
                    align-items: center; 
                    min-height: 100vh; /* Alto mínimo para centrar verticalmente */
                    background-color: #f0f0f0; /* Un color de fondo suave para la página */
                }
                #$canvasId { 
                    /* El tamaño del div donde se dibujará la nube */
                    width: 800px;  /* Ancho del contenedor de la nube */
                    height: 600px; /* Alto del contenedor de la nube */
                    border: 1px solid #cccccc; /* Un borde opcional */
                }
            </style>
        </head>
        <body>
            <div id="$canvasId"></div>

            <script>
                // Espera a que el DOM esté completamente cargado para ejecutar el script
                document.addEventListener('DOMContentLoaded', function() {
                    var canvasElement = document.getElementById('$canvasId');
                    // Convierte el string JSON de opciones a un objeto JavaScript
                    var wordCloudOptions = ${options.toString(2)}; // .toString(2) para indentar el JSON y hacerlo legible

                    // Llama a la función WordCloud para generar la nube
                    WordCloud(canvasElement, wordCloudOptions);
                });
            </script>
        </body>
        </html>
        """.trimIndent() // trimIndent() es útil para eliminar indentaciones extrañas en plantillas de texto
    }
}