#Funciones en python
#1° Dentro del mismo archivo principal
#2° Fuera del archivo principal --> Libreria

#Sintaxis de una funcion

#def NOMBRE (parametros):
  #Codigo
  #Return(variable)

#1° Con parametros
#2° Sin parametros
#3° Con retorno
#4° Sin retorno

# Ejemplo 4 operaciones
import Libreria as oper
# === PROGRAMA PRINCIPAL ===
print("Las cuatro operaciones basicas")
rsp=0
while rsp!=5:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    rsp=int(input("Ingrese una opción: "))
    if rsp==1:
        w=int(input("Ingrese el primer valor: "))
        z=int(input("Ingrese el segundo valor: "))
        oper.sumar(w,z)
    if rsp==2:
        oper.restar()
    if rsp==3:
        w=int(input("Ingrese el primer valor: "))
        z=int(input("Ingrese el segundo valor: "))
        print("La multiplicación de los valores es: ",oper.multiplicar(w,z))
    if rsp==4:
        w=int(input("Ingrese el primer valor: "))
        z=int(input("Ingrese el segundo valor: "))
        print("La división de los valores es: ",oper.dividir(w,z))
    if rsp==5:
        print("Saliendo del programa")