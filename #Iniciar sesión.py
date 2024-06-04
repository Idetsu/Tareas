usr=[]
passwd=[]
ini=True
x=0
z=0
#Registrar con reglas de negocio
#Por desarrollar Registro: Requerir mayuscula y al menos 1 numero
def registrar():
    user=str(input("Registre su nombre de usuario: "))
    usr.append(user)
    password=str(input("Registre su contraseña: "))
    passwd.append(password)
#Por desarrollar Inicio: Crear usuarios independientes, por ahora, mientras ambos datos esten en la
#lista, se puede iniciar sesión, lo que es incorrecto
def iniciar():
    userini=str(input("Ingrese su nombre de usuario: "))
    passwordini=str(input("Ingrese su contraseña: "))
    if userini in usr or passwordini in passwd:
        print("Se ha iniciado sesión.")
        ini=True
        return ini
    else:
        print("Usuario o contraseña incorrectos.")
        ini=False
        return ini

while z!=3:
    print("1.- Registrarse")
    print("2.- Iniciar Sesión")
    print("3.- Salir")
    print("")
    z=int(input("Ingrese una opción: "))
    if z==1:
        registrar()
    if z==2:
        ini=iniciar()
        if ini==True:
           while x!=4:
            print("1.- Comprar ...")
            print("1.- Vender ...")
            print("1.- Ver Dinero")
            print("4.- Salir")
            print("")
            x=int(input("Ingrese una opción: "))
           if x==1:
            print("")
           if x==2:
            print("")
           if x==3:
            print("")
        if ini==False:
           print("No se ha iniciado sesión.")
           break
    if z==3:
        print("Saliendo de la tienda.")
