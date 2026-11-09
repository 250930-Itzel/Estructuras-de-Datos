from collections import deque
import time

cola_turnos = deque()

cola_turnos.append("Ana")
cola_turnos.append("Luis")
cola_turnos.append("Maria")

print("Turnos registrados:")
print(list(cola_turnos))

while len(cola_turnos) > 0:
    cliente = cola_turnos.popleft()
    print("\nAtendiendo a:", cliente)
    time.sleep(1)
    print("Clientes restantes:", len(cola_turnos))

print("\nTodos los clientes han sido atendidos.")
print("Cola final:", list(cola_turnos))
