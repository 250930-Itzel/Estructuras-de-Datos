# Práctica de recursividad en Python

**Asignatura:** Estructura de Datos  
**Unidad:** 2  
**Tema:** Recursividad  
**Repositorio:** [Estructuras-de-Datos](https://github.com/250930-Itzel/Estructuras-de-Datos)

## Objetivo

Resolver tres problemas mediante funciones recursivas en Python, identificando el caso base y el caso recursivo de cada solución.

## Archivos de la práctica

| Archivo | Descripción |
|---|---|
| `ejercicio1_limpiar_feed.py` | Elimina solamente las publicaciones repetidas consecutivamente. |
| `ejercicio2_interes_compuesto.py` | Calcula el saldo acumulado aplicando interés compuesto por cada depósito. |
| `ejercicio3_profundidad_comentarios.py` | Encuentra la profundidad máxima de una lista de comentarios anidados. |

## ¿Qué es la recursividad?

La recursividad es una técnica en la que una función se llama a sí misma para resolver un problema dividiéndolo en partes más pequeñas. Toda función recursiva necesita:

- **Caso base:** condición que detiene las llamadas recursivas.
- **Caso recursivo:** paso que reduce el problema y vuelve a llamar a la función.

## Ejercicio 1. Limpiador de publicaciones repetidas en un Feed

**Función:** `limpiar_feed(publicaciones)`

**Objetivo:** quitar únicamente los duplicados que aparecen de manera consecutiva. Una publicación puede repetirse más adelante si no está junto a otra igual.

**Lógica:**
1. Si la lista tiene cero o un elemento, se devuelve sin cambios (caso base).
2. Se comparan los dos primeros elementos.
3. Si son iguales, se descarta el primero y se procesa el resto.
4. Si son diferentes, se conserva el primero y se concatena con el resultado recursivo del resto.

**Ejemplo:**

```python
limpiar_feed(["Post A", "Post B", "Post B", "Post C", "Post B"])
```

**Resultado esperado:**

```python
["Post A", "Post B", "Post C", "Post B"]
```

**Observación:** no se utilizan ciclos `for` o `while`, de acuerdo con la restricción del ejercicio.

## Ejercicio 2. Proyección de ahorro con interés compuesto

**Función:** `calcular_saldo_final(depositos, tasa_interes)`

**Objetivo:** calcular el saldo acumulado aplicando una tasa fija anual después de sumar cada depósito.

**Fórmula:**

```text
Saldo nuevo = (Saldo anterior + Depósito actual) * (1 + tasa_interes)
```

**Lógica:**
1. Si la lista de depósitos está vacía, se devuelve `0.0` (caso base).
2. Se calcula recursivamente el saldo de los depósitos anteriores.
3. Se suma el último depósito y se aplica la tasa de interés.

**Ejemplo:**

```python
calcular_saldo_final([1000, 2000, 1500], 0.05)
```

| Año | Operación | Saldo |
|---:|---|---:|
| 1 | (0 + 1000) × 1.05 | 1050.0 |
| 2 | (1050 + 2000) × 1.05 | 3202.5 |
| 3 | (3202.5 + 1500) × 1.05 | 4937.625 |

**Resultado esperado:** `4937.625` (redondeado a dos decimales: `4937.63`).

## Ejercicio 3. Profundidad de un hilo de comentarios

**Función:** `maxima_profundidad(comentarios)`

**Objetivo:** determinar el nivel máximo de anidamiento en una lista que contiene comentarios de texto y sublistas con respuestas.

**Lógica:**
1. Si la lista está vacía, su profundidad es `0` (caso base).
2. Se analiza el primer elemento.
3. Si es una sublista, se suma un nivel y se calcula su profundidad recursivamente.
4. Si es texto, su nivel dentro del contenedor actual es `1`.
5. Se calcula también la profundidad del resto de la lista y se devuelve el mayor valor.

**Ejemplo:**

```python
hilo = [
    "Comentario 1",
    ["Respuesta 1.1", ["Respuesta 1.1.1"]],
    "Comentario 2"
]
maxima_profundidad(hilo)
```

**Resultado esperado:** `3`.

## Cómo ejecutar los ejercicios

Abre una terminal en la carpeta `Unidad_2` y ejecuta cada archivo por separado:

```bash
python ejercicio1_limpiar_feed.py
python ejercicio2_interes_compuesto.py
python ejercicio3_profundidad_comentarios.py
```

En algunos equipos el comando puede ser `python3` en lugar de `python`.

## Resultados esperados

| Ejercicio | Resultado |
|---|---|
| 1. Feed | `['Post A', 'Post B', 'Post C', 'Post B']` |
| 2. Ahorro | `4937.625` |
| 3. Profundidad | `3` |

## Conclusión

Con esta práctica se aplicó la recursividad al procesamiento de listas, al cálculo de valores acumulados y al análisis de estructuras anidadas. En los tres ejercicios se identificó un caso base para detener las llamadas y un caso recursivo que reduce el problema hasta obtener el resultado.
