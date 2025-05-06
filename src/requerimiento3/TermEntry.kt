package requerimiento3

/**
 * Representa una entrada de término procesada desde el archivo CSV.
 *
 * @property categoria La categoría a la que pertenece el término.
 * @property variablePrincipal El nombre principal de la variable/término (usado como clave).
 * @property terminosDeBusqueda Lista que incluye la variablePrincipal y todos sus sinónimos,
 * todos convertidos a minúsculas para la búsqueda.
 */
data class TermEntry(
    val categoria: String,
    val variablePrincipal: String,
    val terminosDeBusqueda: List<String>
)