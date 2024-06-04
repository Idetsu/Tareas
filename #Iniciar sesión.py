usr=["oscar"]
passwd=["Oscarm5276"]
ini=True
x=0
z=0
print("Usuario: oscar")
print("Contraseña: Oscarm5276")
print("")
def iniciar():
    userini=str(input("Ingrese su nombre de usuario: "))
    passwordini=str(input("Ingrese su contraseña: "))
    if userini in usr and passwordini in passwd:
        print("Se ha iniciado sesión.")
        ini=True
        return ini
    else:
        print("Usuario o contraseña incorrectos.")
        ini=False
        return ini

while z!=2:
    print("1.- Iniciar Sesión")
    print("2.- Salir")
    print("")
    z=int(input("Ingrese una opción: "))
    if z==1:
        ini=iniciar()
        if ini==True:
           print("1.- Comprar fertilizantes")
           print("2.- Comprar semillas")
           print("3.- Vender verduras")
           print("4.- Consultar Dinero")
           print("5.- Salir")
           print("")
           while x!=4:
            x=int(input("Ingrese una opción: "))
            if x==5:
               print("1.- ")
               print("2.- ")
               print("3.- ")
               print("4.- ")
            if x==2:
                print("asd2")
            if x==3:
             print("asd3")
            if x==4:
             print("asd4")
            if x==5:
             print("asd5")
        if ini==False:
           print("No se ha iniciado sesión.")
           break
    if z==2:
        print("Saliendo de la tienda.")
