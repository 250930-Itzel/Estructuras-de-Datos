lista = [6.8,10,7.4,9,8,7,5,7.8,5.5,7.2,8.8,8.9,9.7,9.4,9.99]
n = len(lista)
swapped = True
while swapped:
    swapped= False
for i in range(n-1):
    if lista [i]>lista[i+1]:
        lista[i],lista[i+1]=lista[i+1],lista[i]
swapped = True
print("Orden Ascendente:",lista)



lista = [6.8,10,7.4,9,8,7,5,7.8,5.5,7.2,8.8,8.9,9.7,9.4,9.99]
n = len(lista)
swapped = True
while swapped:
    swapped= False
for i in range(n-1):
    if lista [i]<lista[i+1]:#solo cambiamos el signo para ir al reves
        lista[i],lista[i+1]=lista[i+1],lista[i]
swapped = True#Esta es la variable booleana por si es verdad o falso
print("Orden Decendente:",lista)