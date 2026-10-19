from collections import deque
cola=deque()
#agregar elementos a la cola (encolar)
cola.append("Cliente 1")
cola.append("Cliente 2")
cola.append("Cliente 3")
#Sacar el primer elemento que llego (descolar)
atendio=cola.popleft()
#Mostrar resultados
print("Atendio ", atendio)
print("cola restante ", cola)