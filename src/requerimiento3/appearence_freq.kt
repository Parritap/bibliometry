package requerimiento3

import java.util.*

fun main() {
    val abstract = "The digital paradigm requires efficient methods of teaching CAAD " +
            "tools in architecture schools. With the trend of enhancing the design process with" +
            " parametric methods, linking architecture with other knowledge areas, such as" +
            " mathematics, is gaining in importance. Equipping future architects with skills" +
            " in algorithmic thinking is yet another challenge for education. This paper describes " +
            "the workflow of an early-stage course addressing this challenge, conducted at the" +
            " Warsaw University of Technology’s Faculty of Architecture. The course focuses on" +
            " the students’ ability to construct complex geometric forms in the digital environment" +
            " by introducing an extensive analytic phase. The students study the geometric" +
            " foundations of real-world architectural cases and translate them into parametric models. " +
            "Later, they explore the potential of the generated solutions space. The results compare the " +
            "course’s teaching efficiency with the outcomes of past courses covering similar subjects."


    println(sortAndCleanAbstract(abstract))

    println()
    val element = "architecture"
    println(
        "Cantidad de concidencias de la palabra 'the': " +
                countWordOccurrences(element, sortAndCleanAbstract(abstract))
    )

    // Z Algorithm


}

/**
 * Esta funcion recibe un abstract y lo convierte a minusculas, lo separa por espacios,
 * tambien elimina los espacios en blanco al principio y al final de cada palabra, y además elimina
 * el punto final de cada palabra si lo tiene.
 */
fun sortAndCleanAbstract(abstract: String): List<String> = abstract
    .lowercase(Locale.getDefault())
    .split(" ")
    .asSequence()
    .map { it.trim() }
    .map { if (it.isNotEmpty() && it.last() == '.') it.dropLast(1) else it }
    .filter { it.isNotEmpty() }
    .sorted()
    .toList()

/**
 * Cuenta la cantidad de veces que aparece una palabra en una lista ordenada.
 * Usa busqueda binaria para encontrar la palabra y luego cuenta las ocurrencias.
 * Cuando el indice donde se encuentra la palabra es menor a 0, significa que no existe.
 * Cuando el indice es mayor o igual a 0, significa que existe, luego el algoritmo busca en lo posible
 * a la derecha y a la izquierda de dicho indice para contar las ocurrencias..
 */
fun countWordOccurrences(word: String, sortedList: List<String>): Int {
    // Find any occurrence with binary search
    val index = Collections.binarySearch(sortedList, word)

    // Word not found
    if (index < 0) {
        return 0
    }

    // Count all occurrences (left and right of found index)
    var count = 1

    // Check left side
    var left = index - 1
    while (left >= 0 && sortedList[left] == word) {
        count++
        left--
    }

    // Check right side
    var right = index + 1
    while (right < sortedList.size && sortedList[right] == word) {
        count++
        right++
    }

    return count
}

/**
 * Cuenta el total de apariciones de todos los términos del conjunto proporcionado en una lista ordenada.
 *
 * Esta función itera a través de cada término en el conjunto dado y cuenta cuántas veces
 * aparece en la lista ordenada especificada. Luego devuelve la suma de todas las apariciones.
 *
 * Ejemplo:
 * Si setOfTerms = {"Object Oriented Programming", "OOP"} y
 * sortedList = {"Object Oriented Programming", "OOP", "OOP", "OOP"},
 * entonces esta función devolverá 4, ya que "OOP" aparece 3 veces y
 * "Object Oriented Programming" aparece una vez.
 *
 * @param setOfTerms Un conjunto de términos a buscar en la lista
 * @param sortedList Una lista ordenada de cadenas en la cual buscar
 * @return El conteo total de apariciones de todos los términos del conjunto
 */
fun countSetOfTerms(setOfTerms: List<String>, sortedList: List<String>): Int {
    var count = 0
    for (term in setOfTerms) {
        count += countWordOccurrences(term, sortedList)
    }
    return count
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

// Implementation of the Z Algorithm por string searching within a text


/*
 * Prints all occurrences of `pattern` in `text` using the Z-algorithm
 */

fun searchWithZ(text: String, pattern: String) {
    // Concatenate pattern, a delimiter, and the text
    val concat = "$pattern\$$text"
    val n = concat.length

    // Z-array to hold lengths of matches with prefix
    val Z = IntArray(n)

    // Build Z-array for the concatenated string
    getZArr(concat, Z)

    // Scan Z-array for full pattern matches
    for (i in Z.indices) {
        if (Z[i] == pattern.length) {
            // Pattern found at index (i - pattern.length - 1) in original text
            println("Pattern found at index ${'$'}{i - pattern.length - 1}")
        }
    }
}

/**
 * Fills the Z-array for string `str`
 * Z[i] = length of the longest substring starting at i matching the prefix
 */
private fun getZArr(str: String, Z: IntArray) {
    val n = str.length
    var L = 0
    var R = 0

    for (i in 1 until n) {
        if (i > R) {
            L = i
            R = i
            while (R < n && str[R - L] == str[R]) {
                R++
            }
            Z[i] = R - L
            R--
        } else {
            val k = i - L
            if (Z[k] < R - i + 1) {
                Z[i] = Z[k]
            } else {
                L = i
                while (R < n && str[R - L] == str[R]) {
                    R++
                }
                Z[i] = R - L
                R--
            }
        }
    }
}

