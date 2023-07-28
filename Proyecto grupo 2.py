import time
import random
import string


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
    print("")
    nombreDeComercio = input("Ingrese el nombre del comercio: ")
    print("")
    telefonoDeComercio = input("Ingrese el teléfono del comercio: ")
    print("")
    nombreDelDueno = input("Ingrese el nombre del dueño: ")
    print("")
    ubicacionDelLocal = input("Ingrese la ubicación del local: ")
    print("")
    file = open("datosUsuarios.txt","a")
    file.write("Correo Electronico: " + correoElectronico)
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
    correoElectronico = buscarCorreo
    usuario = buscarCorreo   
    
    if buscarCorreo == usuario:
        mostrarUsiario()
    else:
        print("")
        print("No se encontró ningún usuario con ese correo.")
        print("")
        
def archivoFactElectronica():
    file=open("facturaElectronica.txt","w")
    file.close()

def crearFactElectronica():
    cedula = input( "Ingrese numero de cedula fisica o juridica: ")
    print("")
    nombre = input(" Nombre de la persona o empresa: ")
    print("")
    numeroTelefonico = input(" Numero de telefono de la persona o empresa: ")
    print("")
    direccionPostal = input("Ingrese la direccion de la casa o empresa: ")
    print("")
    correo= input("Ingrese su correo electronico: ")
    print("")
    file = open("facturaElectronica.txt","a")
    file.write("Cédula: " + cedula)
    file.write("\n")
    file.write("Nombre: " + nombre)
    file.write("\n")
    file.write("Numero de telefono:" + numeroTelefonico)
    file.write("\n")
    file.write("Direccion Postal: " + direccionPostal)
    file.write("\n")
    file.write("Correo: " + correo)
    file.write("\n")
    print("La informacion fue grabada correctamente!")
    file.close()
    respuesta = input(f'¿Desea cambiar un dato? si/no: ')

    if respuesta == 'si':
        cedula = input( "Ingrese numero de cedula fisica o juridica: ")
        print("")
        nombre = input(" Nombre de la persona o empresa: ")
        print("")
        numeroTelefonico = input(" Numero de telefono de la persona o empresa: ")
        print("")
        direccionPostal = input("Ingrese la direccion de la casa o empresa: ")
        print("")
        correo= input("Ingrese su correo electronico: ")
        print("")
        file = open("facturaElectronica.txt","w")
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

import random
import string

codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

print(codigo)
        
def archivoPaquete():
    file=open("datosPaquete.txt","w")
    file.close()
    
def crearPaquete():
    destinatario = input("Ingrese el nombre del destinatario:" )
    print("")
    numeroTelefono = input("Ingrese el número de telefono del Destinatario:" )
    print("")
    cedula = input("Digite el número de cédula:" )
    print("")
    ubicacionDelLocal = input("Ingrese la ubicación del local: ")
    print("")
    peso = input("Ingrese el peso del paquete en Kilogramos:" )
    print("")
    cobro = input("Ingrese forma de pago Tarjeta o Efectivo:" )
    print("")
    print("La informacion fue grabada correctamente!")
    print("")

    if cobro == 'tarjeta':
            pin = input("Dijite el PIN de su tarjeta:" )
            print("")
            monto = input("Monto en colones a Cancelar en la entrega:" )
            print("")
                    

    else:
        monto = input("Monto en colones a Cancelar en la entrega:" )
        print("")
        

    numeroGuia = codigo

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
    print("")
    print("Nombre del destinatario:", destinatario)
    print("")
    print("Número telefónico del destinatario:", numeroTelefono)
    print("")
    print("Número de Cédula:", cedula)
    print("")
    print("Peso total del paquete:", peso, "Kg")
    print("")
    print("Forma de Pago:", cobro)
    print("")
    print("Monto a Cancelar:", monto, "colones")
    print("")
    print("Lugar de entrega:", ubicacionDelLocal)
    print("")
    print("Estado del paquete: Creado")
    print("")


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
    print("6. Rastrear paquete")
    print("")
    print("7. Salir")
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
        numeroGuia = codigo
        respuesta1 = input('¿Ya recibió el paquete ? si/no: ')
        
        if respuesta1 == 'si':
            print("Estado del paquete: Entregado")

        #esperar 5 segundos entre cada mensaje, gracias !   
        else:
            print("Estado del paquete: En ruta")
            print("")
            time.sleep(5)
            print("Estado del paquete: En epera")
            print("")
            time.sleep(5)
            print("Estado del paquete: No se retiro, entrega fallida")
            print("")
            print("Si el estado aparece como entrega fallida, debera a volver a solicitar el envio del paquete")
            print("")

    if opcion == "6":

        while True:
            Rastreo = input("Ingrese el código: ")
            print("")
            
            if Rastreo == codigo:
                print("¡Código correcto!")
                print("")
                break
            else:
                print("Código incorrecto. Inténtelo de nuevo.")
                print("")

        while True:

                Hora = int(input("Ingrese la Hora que en la que esta solicitando el estado del Rastreo cabe recalcar que esta ajustado en horario de 24 horas(Poner la hora sin minutos). "))
                print("")
                if Hora <= 9:
                        print("El paquete se encuentra en Nuestro almacen por favor verifica despues de las 12 M.D ")
                        print("")
                elif Hora <= 12:
                        print("El paquete se encuentra saliendo de nuestro Almacen ")
                        print("")
                elif Hora >= 16:
                        print("El paquete esta por llegar puedes esperar fuera de tu Hogar al repartidor ")
                        print("")
                        
                break

        
    if opcion == "7":
        break

    
     

    

        
        

       
        

