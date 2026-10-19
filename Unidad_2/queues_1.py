from collections import deque
import time
cola_reproduccion = deque()
#El usuario agrega conciones 
cola_reproduccion.append("1.Antologia")
cola_reproduccion.append("2.Historia de Amor")
cola_reproduccion.append("3.Historia entre tus dedos")
print("caoncion en espera")
for cancion in cola_reproduccion:
    print(" _", cancion)
    print("iniciamos reproducion")
#reproductor procesa la cola por cancion (descolar)
while cola_reproduccion:
    cancion_actual = cola_reproduccion.popleft()
    print(f"sonando ahora{cancion_actual}")
    time.sleep#simla canciones que quedan en la cola
    print(f"finalizo: {cancion_actual}")
    #muestra cuantas canciones quedan en la cola
    print(f"Quedan {len(cola_reproduccion)} canciones en cola")
    print("La cola de reproduccion ha terminado.")