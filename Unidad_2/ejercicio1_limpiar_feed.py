"""
Ejercicio 1: Limpiador de publicaciones repetidas en un Feed.

Elimina únicamente los elementos iguales que aparecen uno junto al otro.
No utiliza ciclos for/while ni modifica índices manualmente.
"""


def limpiar_feed(publicaciones: list) -> list:
    """
    Devuelve una lista sin duplicados consecutivos.

    Caso base:
        Una lista con cero o un elemento ya está limpia.

    Caso recursivo:
        Compara los dos primeros elementos. Si son iguales, descarta
        el primero; si son diferentes, conserva el primero. Después
        procesa recursivamente el resto de la lista.

    Args:
        publicaciones: Lista de publicaciones.

    Returns:
        Una nueva lista sin repeticiones consecutivas.
    """
    if len(publicaciones) <= 1:
        return publicaciones

    if publicaciones[0] == publicaciones[1]:
        return limpiar_feed(publicaciones[1:])

    return [publicaciones[0]] + limpiar_feed(publicaciones[1:])


if __name__ == "__main__":
    ejemplo = ["Post A", "Post B", "Post B", "Post C", "Post B"]
    resultado = limpiar_feed(ejemplo)

    print("Publicaciones originales:", ejemplo)
    print("Feed limpio:", resultado)
    # Resultado esperado:
    # ['Post A', 'Post B', 'Post C', 'Post B']
