package requerimiento3

import java.util.*
import kotlin.math.abs

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
            "course’s teaching efficiency with the outcomes of past courses covering similar subjects." +
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
    val coincidences = searchCompoundTerm("teaching efficiency with", abstract)
    print(coincidences)

}

/**
 * If any term in list of terms is a compound one, i.e, has more than one word, then Z algorithm with original abstract is used
 * If not, then, another algorithm is used -> The abstract is sorted and then the single word term is search
 * effienctly using binary search.
 * @param abstract shouldnt be sorted in this function.
 */
fun countTerms(terms: List<String>, abstract: String) : Int {
    var count = 0
    for (term in terms) {
        if (term.split(" ").size >= 2) count += searchCompoundTerm(term, abstract)
        else count += countWordOccurrences(term, sortAndCleanAbstract(abstract))
    }
    return count
}

/**
 * Esta funcion recibe un abstract y lo convierte a minusculas, lo separa por espacios,
 * tambien elimina los espacios en blanco al principio y al final de cada palabra, y además elimina
 * el punto final de cada palabra si lo tiene.
 */
fun sortAndCleanAbstract(abstract: String): List<String> = abstract
    .lowercase(Locale.getDefault())
    .split("\\s+".toRegex())
    .asSequence()
    .map { it.trim().replace(Regex("""^\p{Punct}+|\p{Punct}+$"""), "") }
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
fun countSetOfTermsSorted(setOfTerms: List<String>, sortedList: List<String>): Int {
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



fun searchCompoundTerm(term: String, abstract: String) = zAlgorithm(
    term.lowercase(Locale.getDefault()),
    abstract.lowercase(Locale.getDefault())
).size


/**
 * Computes the Z-array for a given string s.
 * Z[i] = length of the longest substring starting at i
 * which is also a prefix of s.
 */
fun calculateZ(s: String): IntArray {
    val n = s.length
    val z = IntArray(n)
    var l = 0
    var r = 0

    for (i in 1 until n) {
        if (i > r) {
            // Case 1: i is outside the current Z-box
            l = i
            r = i
            while (r < n && s[r] == s[r - l]) {
                r++
            }
            z[i] = r - l
            r--
        } else {
            // Case 2: i is inside the current Z-box
            val k = i - l
            if (z[k] < r - i + 1) {
                // Case 2a: z[k] does not stretch outside the box
                z[i] = z[k]
            } else {
                // Case 2b: z[k] might stretch outside, so we compare manually
                l = i
                while (r < n && s[r] == s[r - l]) {
                    r++
                }
                z[i] = r - l
                r--
            }
        }
    }
    return z
}

/**
 * Finds all occurrences of `pattern` in `text` using the Z-algorithm.
 * Returns a list of starting indices in `text`.
 */
fun zAlgorithm(pattern: String, text: String): List<Int> {
    // Combine pattern, a delimiter not in pattern/text, and text
    val combined = pattern + "$" + text
    val z = calculateZ(combined)
    val m = pattern.length
    val result = mutableListOf<Int>()

    for (i in z.indices) {
        if (z[i] == m) {
            // i - m - 1 compensates for pattern + delimiter
            result.add(i - m - 1)
        }
    }
    return result
}

