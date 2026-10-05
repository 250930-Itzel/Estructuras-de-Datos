import matplotlib.pyplot as plt 
datos = [42, 12, 88, 23, 7, 65, 34, 50]
#Algoritmo de insercion
def insercion(arr):
    a = arr.copy()
    comp = 0
    for i in range(1, len(a)):
        clave, j=a[i],i-1
        while j>=0 and a[j]>clave:
            comp += 1
        a[j+1] = a[j]
        j-=1
        if j>=0:comp += 1
        a[j+1]= clave
        return a, comp
#Algoritmo de Seleccion
def seleccion (arr):
    a = arr.copy()
    comp = 0
    n = len (a)
    for i in range(n):
        min_idx=i
        for j in range (i+1, n):
            comp += 1
            if a[j]< a[min_idx]:
                min_idx=j
                a[j], a[min_idx]= a[min_idx], a[i]
    return a,comp

#Ejecutamos ambos algoritmos
lista_ordenada, comp_ins =insercion(datos)
_,comp_Sel = seleccion(datos)

#Graficacion
fig,(ax1,ax2,ax3)= plt.subplots(1,3,figsize=(12, 3.5))

#Grafico 1 inicial-lista desordenada
ax1.bar(range(len(datos)), datos, color='salmon')
ax1.set_title('1.- Lista desordenada')
ax1.set_ylabel('valor')
            
#Grafico 2-Lista oredenada
ax2.bar(range(len(lista_ordenada)), lista_ordenada, color='green')
ax2.set_title('2.- Lista ordenada')  

#Grafico 3 comparaciones realizadas
ax3.bar(['interseccion', 'seleccion'], [comp_ins,comp_Sel], color=["#2397EA", "#ac8059"])
ax3.set_title('3.- Comparaciones')
ax3.set_ylabel('cantidad')

plt.tight_layout()
plt.show()
                 
