#Trabajo grupo 2 mensajeria Fidelitas



#Parte Diana y Franco (Registrar una cuenta de usuario)
print("")
print(" Bienvenido(a) a Mensajeria Fidelitas")
print("")


# Variables

correoElectronico = 0

nombreDeComercio = 0

telefonoDeComercio = 0

nombreDelDueno = 0

ubicacionDelLocal= 0

paquetes = {}

respuesta = 'si'
respuesta == 'no'

cobro = 'tarjeta'
cobro == 'efectivo'

while True:
    print("")
    print("1. Crear cuenta de usuario")
    print("")
    print("2. Buscar usuario")
    print("")
    print("3. Crear factura electronica")
    print("")
    print("4. Crear un paquete")
    print("")
    print("5. Ver estado del paquete")
    print("")
    print("6. Salir")
    print("")

    opcion = input("Ingrese una opción: ")


    if opcion == '1':

        #Registro de cuenta de usuario

        correoElectronico = input(" Ingrese su correo electrónico: ")
        nombreDeComercio = input("Ingrese el nombre del comercio: ")
        telefonoDeComercio = input("Ingrese el teléfono del comercio: ")
        nombreDelDueno = input("Ingrese el nombre del dueño: ")
        ubicacionDelLocal = input("Ingrese la ubicación del local: ")

        # Imprimir los datos ingresados
        print("Datos de la cuenta registrada:")
        print("")
        print("Correo electrónico:", correoElectronico)
        print("")
        print("Nombre del comercio:", nombreDeComercio)
        print("")
        print("Teléfono del comercio:", telefonoDeComercio)
        print("")
        print("Nombre del dueño:", nombreDelDueno)
        print("")
        print("Ubicación del local:", ubicacionDelLocal)
        print("")
        print("Cuenta creada exitosamente.")

        #Diana

    elif opcion == '2':
        
        buscarCorreo = input("Ingrese el correo del usuario a buscar: ")
        usuario = correoElectronico
        

        if usuario == buscarCorreo:

            print("Correo electrónico:", correoElectronico)
            print("")
            print("Nombre del comercio:", nombreDeComercio)
            print("")
            print("Teléfono del comercio:", telefonoDeComercio)
            print("")
            print("Nombre del dueño:", nombreDelDueno)
            print("")
            print("Ubicación del local:", ubicacionDelLocal)
            print("")

        else :
            print("")
            print("No se encontró ningún usuario con ese correo.")
            print("")



#Parte Daryl y Alex(Registro de factura electrónica)

    if opcion == '3':
        #Registro de factura electronica
        cedula = input( "Ingrese numero de cedula fisica o juridica: ")
        nombre = input(" Nombre de la persona o empresa: ")
        numeroTelefonico = input(" Numero de telefono de la persona o empresa: ")
        direccionPostal = input("Ingrese la direccion de la casa o empresa: ")
        correo= input("Ingrese su correo electronico: ")
        respuesta = input(f'¿Desea cambiar un dato? si/no: ')

        if respuesta == 'si':
            cedula = input( "Ingrese numero de cedula fisica o juridica: ")
            nombre = input(" Nombre de la persona o empresa: ")
            numeroTelefonico = input(" Numero de telefono de la persona o empresa: ")
            direccionPostal = input("Ingrese la direccion de la casa o empresa: ")
            correo= input("Ingrese su correo electronico: ")
            print("Datos para la factura electronica:")
            print("cedula fisica o juridica: ", cedula)
            print("Nombre de la persona o empresa: ",nombre)
            print("Numero telefonico de la persona o empresa: ",numeroTelefonico)
            print("Direccion de la casa o empresa: ",direccionPostal)
            print("Correo electronico: ",correo)
            
        else:
            respuesta == 'no'
            print("Datos para la factura electronica:")
            print("cedula fisica o juridica: ", cedula)
            print("Nombre de la persona o empresa: ",nombre)
            print("Numero telefonico de la persona o empresa: ",numeroTelefonico)
            print("Direccion de la casa o empresa: ",direccionPostal)
            print("Correo electronico: ",correo)
            print("Gracias por su compra")
            

  
#Parte Anthony (Creación de paquete)
            
    if opcion == '4':

        #Datos para creación de paquetes

        destinatario = input("Ingrese el nombre del destinatario:" )
        numeroTelefono = int(input("Ingrese el número de telefono del Destinatario:" ))
        cedula = int(input("Digite el número de cédula:" ))
        peso = float(input("Ingrese el peso del paquete en Kilogramos:" ))
        cobro = input("Ingrese forma de pago Tarjeta o Efectivo:" )

        if cobro == 'tarjeta':
            pin = int(input("Dijite el PIN de su tarjeta:" ))
            monto = float(input("Monto en colones a Cancelar en la entrega:" ))

        else:
            cobro == 'efectivo'
            monto = float(input("Monto en colones a Cancelar en la entrega:" ))

        #Impirmir los datos

        print("Nombre del destinatario:", destinatario)
        print("Numero telefonico del destinario:", numeroTelefono)
        print("Número de Cédula: ", cedula)
        print("Peso total del paquete:", peso)
        print("Forma de Pago:", cobro)
        print("Monto a Cancelar:" , monto)
        print("Lugar de entrega:", ubicacionDelLocal)

#CAMBIO DE ESTADO DE PAQUETE ANTHONY Y DARYL
    if opcion == '5':
        guia = int(input("Ingrese el número de guía del paquete:"))

        if guia in paquetes:
            paquete = paquetes[guia]
            if paquete["estado"] == "En tránsito":
                tiempo_actual = time.time()
                tiempo_creacion = paquete["tiempo_creacion"]
                if tiempo_actual - tiempo_creacion >= 20:
                    paquete["estado"] = "Entregado"
                    print("El paquete ha sido entregado.")    
        
    elif opcion == '6':
        break

    else:
        print("Opción inválida. Intente nuevamente.")
