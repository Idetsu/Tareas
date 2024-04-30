#Estructura de datos: Listas

import random as rd #as para cambiar el nombre de la libreria, en este caso ahora se llama: rd

lista_1=[] #lista vacia
lista_2=[5,"Juan",18.5,-8,True,"Lopez"] #lista con datos

print(lista_2[4]) #Una lista empieza de 0, por tanto no se muestra -8 (posicion 3), sino True (posicion 4)
print(lista_2,("Vista developer")) # Vista developer

for w in (lista_2): #Vista usuario
    print(w,end=" ") #Mostrar datos hacia al lado, el " " es para separar

# OPERACIONES CON UNA LISTA 
    #lista.append(dato)
    #lista.insert(x,y)  // x=posicion  y=dato  //va hacia la posicion x e inserta el dato y
    #Ejemplo, lista.insert(3,5), va hacia la posicion 3 e inserta el numero entero: 5

    #lista.remove() //elimina un dato POR SU NOMBRE, NOTA: elimina solo 1 dato aunque este repetido, el primero que encuentre
    #si se quiere eliminar mas de un dato se necesita usar un ciclo

    #lista.pop() //Elimina el -1 si no tiene datos, elimina una POSICION
    #lista.pop(3) //Elimina la posicion 3

    #lista.count("Lopez") //Cuenta cuantos "Lopez" hay en la lista

    #lista.sort(reverse=true) //Ordena de mayor a menor, pero al usar reverse queda de menor a mayor


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
