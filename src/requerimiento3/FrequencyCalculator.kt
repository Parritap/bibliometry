package requerimiento3

// No necesitamos importar explícitamente las funciones de appearance_freq.kt
// si FrequencyCalculator.kt está en el mismo paquete (requerimiento3)
// y las funciones en appearance_freq.kt son de nivel superior (top-level) o públicas.

object FrequencyCalculator {

    /**
     * Calcula las frecuencias de los términos en una lista de abstracts.
     *
     * @param termEntries La lista de TermEntry obtenida del CSVParser.
     * @param abstracts La lista de strings, donde cada string es el texto de un abstract.
     * @return Un Par (Pair) donde:
     * - el primer elemento es un Mapa de frecuencias por categoría: Map<Categoria, Map<VariablePrincipal, Frecuencia>>
     * - el segundo elemento es un Mapa de frecuencias totales: Map<VariablePrincipal, FrecuenciaTotal>
     */
    fun calculateFrequencies(
        termEntries: List<TermEntry>,
        abstracts: List<String>
    ): Pair<Map<String, Map<String, Int>>, Map<String, Int>> {

        val frequenciesByCategory = mutableMapOf<String, MutableMap<String, Int>>()
        val totalFrequencies = mutableMapOf<String, Int>()

        // Pre-procesamos cada abstract una sola vez para eficiencia:
        // Creamos una lista de pares, donde cada par contiene:
        // 1. El abstract original en minúsculas (para searchCompoundTerm).
        // 2. La lista de palabras del abstract limpiada y ordenada (para countWordOccurrences).
        val processedAbstracts = abstracts.map { abstractText ->
            val lowerAbstract = abstractText.lowercase(java.util.Locale.getDefault())
            // Usamos la función sortAndCleanAbstract de appearance_freq.kt (o donde esté definida)
            val cleanedSortedWords = sortAndCleanAbstract(lowerAbstract)
            lowerAbstract to cleanedSortedWords
        }

        for (entry in termEntries) {
            var accumulatedFrequencyForVariable = 0 // Frecuencia de esta variablePrincipal en todos los abstracts

            for ((lowerAbstract, cleanedSortedWords) in processedAbstracts) {
                var frequencyInThisAbstractForThisEntry = 0
                // Iteramos sobre todos los términos de búsqueda (variable principal + sinónimos)
                for (termToSearch in entry.terminosDeBusqueda) {
                    // termToSearch ya debería estar en minúsculas desde CSVParser
                    if (termToSearch.contains(" ")) {
                        // Es un término compuesto, usamos searchCompoundTerm del abstract original en minúsculas
                        // Asumimos que searchCompoundTerm está disponible (desde appearance_freq.kt)
                        frequencyInThisAbstractForThisEntry += searchCompoundTerm(termToSearch, lowerAbstract)
                    } else if (termToSearch.isNotEmpty()) {
                        // Es un término simple, usamos countWordOccurrences de la lista de palabras limpias y ordenadas
                        // Asumimos que countWordOccurrences está disponible (desde appearance_freq.kt)
                        frequencyInThisAbstractForThisEntry += countWordOccurrences(termToSearch, cleanedSortedWords)
                    }
                }
                accumulatedFrequencyForVariable += frequencyInThisAbstractForThisEntry
            }

            // Almacenar frecuencia por categoría (usando la variablePrincipal de TermEntry como clave)
            // La variablePrincipal en TermEntry mantiene el caso original del CSV, lo cual es bueno para etiquetas.
            frequenciesByCategory.getOrPut(entry.categoria) { mutableMapOf() }
                .merge(entry.variablePrincipal, accumulatedFrequencyForVariable, Int::plus)

            // Almacenar frecuencia total (usando la variablePrincipal de TermEntry como clave)
            totalFrequencies.merge(entry.variablePrincipal, accumulatedFrequencyForVariable, Int::plus)
        }

        return Pair(frequenciesByCategory, totalFrequencies)
    }
}