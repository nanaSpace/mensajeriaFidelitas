import time

respuesta = 'si'
respuesta == 'no'

respuesta1 = 'si'
respuesta1 == 'no'

cobro = 'tarjeta'
cobro == 'efectivo'

correoElectronico = ""
nombreDeComercio = ""
telefonoDeComercio = ""
nombreDelDueno = ""
ubicacionDelLocal = ""

correoElectronico = 0

nombreDeComercio = 0

telefonoDeComercio = 0

nombreDelDueno = 0

ubicacionDelLocal= 0

paquetes = {}

def archivoUsuarios():
    file=open("datosUsuarios.txt","w")
    file.close()
    
def crearUsuario():
    correoElectronico = input(" Ingrese su correo electrónico: ")
    nombreDeComercio = input("Ingrese el nombre del comercio: ")
    telefonoDeComercio = input("Ingrese el teléfono del comercio: ")
    nombreDelDueno = input("Ingrese el nombre del dueño: ")
    ubicacionDelLocal = input("Ingrese la ubicación del local: ")
    file = open("datosUsuarios.txt","a")
    file.write("COrreo Electronico: " + correoElectronico)
    file.write("\n")
    file.write("Nombre del comercio: " + nombreDeComercio)
    file.write("\n")
    file.write("Telefono del comercio: " + telefonoDeComercio)
    file.write("\n")
    file.write("Nombre del dueño: " + nombreDelDueno)
    file.write("\n")
    file.write("Ubicacion del local: " + ubicacionDelLocal)
    file.write("\n")
    print("La informacion fue grabada correctamente!")
    file.close()
    
def mostrarUsiario():
    file=open("datosUsuarios.txt","r")
    mensaje = file.read()
    print(mensaje)
    file.close()

def buscarUsuario():
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

def archivoFactElectronica():
    file=open("facturaElectronica.txt","w")
    file.close()

def crearFactElectronica():
    cedula = input( "Ingrese numero de cedula fisica o juridica: ")
    nombre = input(" Nombre de la persona o empresa: ")
    numeroTelefonico = input(" Numero de telefono de la persona o empresa: ")
    direccionPostal = input("Ingrese la direccion de la casa o empresa: ")
    correo= input("Ingrese su correo electronico: ")
    file = open("facturaElectronica.txt","a")
    file.write(cedula)
    file.write("\n")
    file.write(nombre)
    file.write("\n")
    file.write(numeroTelefonico)
    file.write("\n")
    file.write(direccionPostal)
    file.write("\n")
    file.write(correo)
    file.write("\n")
    print("La informacion fue grabada correctamente!")
    file.close()
    respuesta = input(f'¿Desea cambiar un dato? si/no: ')

    if respuesta == 'si':
        cedula = input( "Ingrese numero de cedula fisica o juridica: ")
        nombre = input(" Nombre de la persona o empresa: ")
        numeroTelefonico = input(" Numero de telefono de la persona o empresa: ")
        direccionPostal = input("Ingrese la direccion de la casa o empresa: ")
        correo= input("Ingrese su correo electronico: ")
        file = open("facturaElectronica.txt","a")
        file.write("Cédula: " + cedula)
        file.write("\n")
        file.write("Nombre:" + nombre)
        file.write("\n")
        file.write("Numero de telefono: " +numeroTelefonico)
        file.write("\n")
        file.write("Direccion: " + direccionPostal)
        file.write("\n")
        file.write("Correo Electronico: " + correo)
        file.write("\n")
        print("La informacion fue grabada correctamente!")
        file.close()
        file=open("facturaElectronica.txt","r")
        mensaje = file.read()
        print(mensaje)
        file.close()
            
    else:
        respuesta == 'no'
        file=open("facturaElectronica.txt","r")
        mensaje = file.read()
        print(mensaje)
        file.close()

def generar_numero_guia():
    return int(time.time())
        
def archivoPaquete():
    file=open("datosPaquete.txt","w")
    file.close()
    
def crearPaquete():
    destinatario = input("Ingrese el nombre del destinatario:" )
    numeroTelefono = input("Ingrese el número de telefono del Destinatario:" )
    cedula = input("Digite el número de cédula:" )
    peso = input("Ingrese el peso del paquete en Kilogramos:" )
    cobro = input("Ingrese forma de pago Tarjeta o Efectivo:" )
    print("La informacion fue grabada correctamente!")

    if cobro == 'tarjeta':
            pin = input("Dijite el PIN de su tarjeta:" )
            monto = input("Monto en colones a Cancelar en la entrega:" )
                    

    else:
        monto = input("Monto en colones a Cancelar en la entrega:" )
        

    numeroGuia = generar_numero_guia()

        # Guardar el paquete en el diccionario
    paquete = {
        "destinatario": destinatario,
        "numeroTelefono": numeroTelefono,
        "cedula": cedula,
        "peso": peso,
        "cobro": cobro,
        "monto": monto,
        "ubicacionDelLocal": ubicacionDelLocal,
        "estado": "En tránsito",  # Asumimos que el paquete se encuentra en tránsito al crearse.
        "tiempo_creacion": time.time(),  # Guardamos el tiempo de creación del paquete.
    }

    paquetes[numeroGuia] = paquete

    print("Número de Guía:", numeroGuia)
    print("Nombre del destinatario:", destinatario)
    print("Número telefónico del destinatario:", numeroTelefono)
    print("Número de Cédula:", cedula)
    print("Peso total del paquete:", peso, "Kg")
    print("Forma de Pago:", cobro)
    print("Monto a Cancelar:", monto, "colones")
    print("Lugar de entrega:", ubicacionDelLocal)
    print("Estado del paquete: Creado")


def mostrarDatosPaquete():
    file=open("datosPaquete.txt","r")
    mensaje = file.read()
    print(mensaje)
    file.close()


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
        archivoUsuarios()
        crearUsuario()
        mostrarUsiario()
    if opcion == '2':
        buscarUsuario()
    if opcion == '3':
        archivoFactElectronica()
        crearFactElectronica()
    if opcion == '4':
        archivoPaquete()
        crearPaquete()
        mostrarDatosPaquete()
    if opcion == '5':
        import time
        numeroGuia = generar_numero_guia()
        respuesta1 = input('¿Ya recibió el paquete ? si/no: ')
        
        if respuesta1 == 'si':
            print("Estado del paquete: Entregado")
            
        else:
            print("Estado del paquete: En ruta")
            time.sleep(5)
            print("Estado del paquete: En epera")
            time.sleep(5)
            print("Estado del paquete: No se retiro, entrega fallida")
            print("Si el estado aparece como entrega fallida, debera a volver a solicitar el envio del paquete")
            
    if opcion == "6":
        break

    
     

    

        
        

