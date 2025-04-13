package bibliometry.logic
// author = {LastName1, FirstName1  and  LastName2, FirstName2  and  LastName3, FirstName3  and  LastName4, FirstName4},

fun getAuthorsFromLine(line: String): List<String> =
    line.split(" and ")
        .map { it.trim() }
        .filter { it.isNotEmpty() }
        .map { author ->
            val parts = author.split(",")
            if (parts.size == 2) {
                "${parts[1].trim()} ${parts[0].trim()}"
            } else {
                author.trim()
            }
        }
        .toList()

fun main() {
    val line = "LastName1, FirstName1 and LastName2, FirstName2 and LastName3, FirstName3 and LastName4, FirstName4"
    val authors = getAuthorsFromLine(line)
    println(authors) // Output: [FirstName1 LastName1, FirstName2 LastName2, FirstName3 LastName3, FirstName4 LastName4]
}
