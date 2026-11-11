"""
Ejercicio 2: Proyección de ahorro con interés compuesto.

Calcula el saldo final aplicando la tasa anual después de sumar
cada depósito al saldo acumulado.
"""


def calcular_saldo_final(depositos: list, tasa_interes: float) -> float:
    """
    Calcula recursivamente el saldo final de una secuencia de depósitos.

    Fórmula por año:
        Saldo nuevo = (saldo anterior + depósito actual) * (1 + tasa)

    Caso base:
        Si no hay depósitos, el saldo es 0.0.

    Caso recursivo:
        Calcula el saldo de todos los depósitos anteriores y después
        incorpora el último depósito con su interés correspondiente.

    Args:
        depositos: Cantidades depositadas al final de cada año.
        tasa_interes: Tasa anual expresada como decimal (5 % = 0.05).

    Returns:
        Saldo acumulado como número decimal.
    """
    if not depositos:
        return 0.0

    saldo_anterior = calcular_saldo_final(depositos[:-1], tasa_interes)
    return (saldo_anterior + depositos[-1]) * (1 + tasa_interes)


if __name__ == "__main__":
    cantidades = [1000, 2000, 1500]
    tasa = 0.05
    resultado = calcular_saldo_final(cantidades, tasa)

    print("Depósitos:", cantidades)
    print("Tasa anual:", tasa * 100, "%")
    print("Saldo final:", resultado)
    print("Saldo final redondeado a 2 decimales:", round(resultado, 2))
    # Resultado esperado: 4937.625 (4937.63 redondeado a 2 decimales)
