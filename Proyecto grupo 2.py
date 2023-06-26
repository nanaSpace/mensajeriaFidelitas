#Trabajo grupo 2 mensajeria Fidelitas



#Parte Diana y Franco (Registrar una cuenta de usuario)



#Parte Daryl y Alex(Registro de factura electrónica)
SI = S
NO = N

if opcion == "3":
    #Registro de factura electronica
    cedula = input( "Ingrese numero de cedula fisica o juridica: ")
    nombre = input(" Nombre de la persona o empresa: ")
    numeroTelefono = input(" Numero de telefono de la persona o empresa: ")
    direccionPostal = input("Ingrese la direccion de la casa o empresa: ")
    correo= input("Ingrese su correo electronico: ")

    #Imprimir todos los datos ingresados por el usuario
    print("Datos para la factura electronica:")
    print("cedula fisica o juridica: ", cedula)
    print("Nombre de la persona o empresa: ",nombre)
    print("Numero telefonico de la persona o empresa: ",numeroTelefonico)
    print("Direccion de la casa o empresa: ",direccionPostal)
    print("Correo electronico: ",correo)
    print("¿Toda la informasion es correcta?: ")
    pregunta = print("¿Desea cambiar un dato? S/N: ")

if pregunta == S:
    pregunta2 = print("¿Que dato desea cambiar?,cedula,nombre,numeroTelefonico,direccionPostal,correo: ")
else:
    if pregunta2 == cedula:
        print("Ingrese el nuevo dato: ")
    elif pregunta2 == nombre:
        print("Ingrese el nuevo dato: ")
    elif pregunta2 == numeroTelefonico:
        print("Ingrese el nuevo dato: ")
    elif pregunta2 == direccionPostal:
        print("Ingrese el nuevo dato: ")
    elif pregunta2 == correo:
        print("Ingrese el nuevo dato: ")
        
        
    
    





#Parte Martines (Creación de paquetes)
