def sumar(a,b):
    suma=a+b
    print("La suma de los valores es: ",suma)
def restar():
    a=int(input("Ingrese el primer valor: "))
    b=int(input("Ingrese el segundo valor: "))
    resta=a-b
    print("La resta de los valores es: ",resta)
def multiplicar(a,b):
    mult=a*b
    return(mult)
def dividir(a,b):
    if b==0:
        print("No se puede dividir por cero")
    else:
        divi=a/b
        print("La división de los valores es: ",divi)