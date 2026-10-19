historial_navegacion=[]
#Operador para apilar(push)
historial_navegacion.append("google.com")
historial_navegacion.append("youtube.com")
historial_navegacion.append("wikipedia.org")
print("historial cargando" , historial_navegacion)

#Operacion cima (top-peek)
pagina_actual = historial_navegacion[-1]
print("pgins sctual en paltalla: ",  pagina_actual)

#Operacion para desampilar(pop)
pagina_cerrada = historial_navegacion.pop()
print("salido de: ", pagina_cerrada)
print("historial despues de presionar 'Atras' ", historial_navegacion)

#Operacion tamaño(size)
total_paginas=len(historial_navegacion)
