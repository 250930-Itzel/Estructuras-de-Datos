"""
Ejercicio 3: Medir la profundidad de un hilo de comentarios.

Las respuestas se representan mediante listas anidadas.
La función calcula el nivel máximo de anidamiento usando recursividad.
"""


def maxima_profundidad(comentarios: list) -> int:
    """
    Obtiene el nivel máximo de profundidad de una lista de comentarios.

    Caso base:
        Una lista vacía tiene profundidad 0.

    Caso recursivo:
        Se analiza el primer elemento y luego el resto de la lista.
        Un texto ocupa el nivel 1 del contenedor actual. Una sublista
        agrega un nivel y se calcula su profundidad recursivamente.

    Args:
        comentarios: Lista con textos y posibles sublistas de respuestas.

    Returns:
        La profundidad máxima como entero.
    """
    if not comentarios:
        return 0

    primero = comentarios[0]

    if isinstance(primero, list):
        profundidad_primero = 1 + maxima_profundidad(primero)
    else:
        profundidad_primero = 1

    profundidad_resto = maxima_profundidad(comentarios[1:])
    return max(profundidad_primero, profundidad_resto)


if __name__ == "__main__":
    hilo = [
        "Comentario 1",
        ["Respuesta 1.1", ["Respuesta 1.1.1"]],
        "Comentario 2"
    ]

    resultado = maxima_profundidad(hilo)
    print("Hilo de comentarios:", hilo)
    print("Profundidad máxima:", resultado)
    # Resultado esperado: 3
