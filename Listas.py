#Estructura de datos: Listas

import random as rd #as para cambiar el nombre de la libreria, en este caso ahora se llama: rd

lista_1=[] #lista vacia
lista_2=[5,"Juan",18.5,-8,True,"Lopez"] #lista con datos

print(lista_2[4]) #Una lista empieza de 0, por tanto no se muestra -8 (posición 3), sino True (posición 4)
print(lista_2,("Vista developer")) # Vista developer

for w in (lista_2): #Vista usuario
    print(w,end=" ") #Mostrar datos hacia al lado, el " " es para separar

#lista_1.append(23)
#print(lista_1)

#llenar lista de numeros aleatorios:
for z in range (10): #cuantos numeros
    n=rd.randint(1,50) #variable numeros aleatorios
    lista_1.append(n) #llenar la lista de n (nombre de variable de numeros aleatorios)

for z in (lista_1):
    print(z,end=" ",)

#======= ORDENAR ======= (debe tener solo numeros o letras,no ambos, se ordena de menor a mayor y de A-Z)
lista_1.sort() #Esto ordena de menor a mayor
print("")
for z in (lista_1):
    print(z,end=" ")

#======= Dar vuelta una lista =======
lista_1.reverse()
print("")
for z in (lista_1):
    print(z,end=" ")

#======= Operaciones con listas =======
print("La suma de las listas es: ",sum(lista_1))
print("el elemento mayor es: ",max(lista_1))
print("el elemento menor es: ",min(lista_1))
print("al promedio de los valores es: ",(sum(lista_1)/len(lista_1)))