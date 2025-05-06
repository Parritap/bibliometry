package requerimiento3

import java.io.InputStream // Necesaria para leer el archivo como un flujo

/**
 * Objeto singleton para parsear el archivo CSV que contiene los términos y categorías.
 */
object CSVParser {

    /**
     * Parsea un InputStream del archivo CSV y lo convierte en una lista de objetos TermEntry.
     *
     * @param inputStream El flujo de entrada del archivo CSV.
     * @return Una lista de objetos TermEntry.
     */
    fun parseTermsCsv(inputStream: InputStream): List<TermEntry> {
        val entries = mutableListOf<TermEntry>()

        // Usamos bufferedReader y useLines para manejar el cierre del stream automáticamente
        // y procesar el archivo línea por línea de manera eficiente.
        inputStream.bufferedReader().useLines { lines ->
            lines.drop(1) // Omitimos la primera línea (la cabecera del CSV)
                .forEach { line ->
                    // Dividimos la línea por comas. Considerar una librería CSV más robusta
                    // si el CSV puede tener comas dentro de campos entrecomillados.
                    val parts = line.split(",").map { it.trim() }

                    if (parts.size >= 2) { // Necesitamos al menos Categoría y Variable
                        val categoria = parts[0]
                        val variablePrincipal = parts[1] // Esta es la clave que usaremos

                        // Los sinónimos están en la tercera columna (índice 2), si existe
                        val sinonimosRaw = if (parts.size >= 3) parts[2] else ""

                        val terminosDeBusqueda = mutableListOf(variablePrincipal.lowercase())

                        if (sinonimosRaw.isNotBlank()) {
                            sinonimosRaw.split("|") // Los sinónimos están separados por "|"
                                .map { it.trim().lowercase() } // Limpiar espacios y convertir a minúsculas
                                .filter { it.isNotEmpty() } // Evitar sinónimos vacíos
                                .forEach { sinonimo ->
                                    terminosDeBusqueda.add(sinonimo)
                                }
                        }

                        // Creamos el TermEntry con la variable principal y la lista completa y única de términos de búsqueda
                        entries.add(
                            TermEntry(
                                categoria = categoria,
                                variablePrincipal = variablePrincipal, // Mantenemos el caso original para la clave/etiqueta
                                terminosDeBusqueda = terminosDeBusqueda.distinct() // Aseguramos términos únicos
                            )
                        )
                    }
                }
        }
        return entries
    }
}