#Iniciar sesión
usr=[]
passwd=[]
password=0
ini=True
def registrar():
    user=0(input("Registre su nombre de usuario: "))
    usr.append(user)
    password=0(input("Registre su contraseña: "))
    passwd.append(password)
def iniciar():
    userini=0(input("Ingrese su nombre de usuario: "))
    passwordini=0(input("Ingrese su contraseña: "))
    if userini in usr or passwordini in passwd:
        print("Se ha iniciado sesión.")
        ini=True
    else:
        print("Usuario o contraseña incorrectos.")
        ini=False

#Menú
#1.- Comprar (producto)
#2.- Vender (producto)
#3.- Ver dinero
#4.- Salir
x=0
z=0
while z!=3:
    print("")
    print("1.- Registrarse")
    print("2.- Iniciar Sesión")
    print("3.- Salir")
    if z==1:
        registrar()
    if z==2:
        iniciar()
        if ini==True:
           while x!=4:
            print("1.- Comprar ...")
            print("1.- Vender ...")
            print("1.- Ver Dinero")
            print("4.- Salir")
           if x==1:
            print("")
           if x==2:
            print("")
           if x==3:
            print("")
        elif ini==False:
           print("No se ha iniciado sesión.")
    else:
        print("Se ha cerrado sesión.")
    if z==3:
        print("Saliendo de la tienda.")