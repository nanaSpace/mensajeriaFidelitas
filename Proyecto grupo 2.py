import time
import random
import string
import sqlite3

respuesta = 'si'
respuesta ='no'

respuesta1 = 'si'
respuesta1 = 'no'

cobro = 'tarjeta'
cobro = 'efectivo'

pregunta = 'si'
pregunta = 'no'

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

cantidad_envios = 0
lista_paquetes_enviados = []
monto_total_cobro = 0
cantidad_paquetes_telefono = {}
cantidad_paquetes_cedula = {}




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
    NumerodeCedula = input("Agregue su numero de cedula: ")
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
    file.write("numero de cedula: " + NumerodeCedula)
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
    correo= input("Ingrese su correo electronico: ")
    print("")
    provincia= input("Provincia: ")
    print("")
    canton=input("Canton: ")
    print("")
    distrito= input("Distrito: ")
    print("")
    file = open("facturaElectronica.txt","w")
    file.write("Cédula: " + cedula)
    file.write("\n")
    file.write("Nombre: " + nombre)
    file.write("\n")
    file.write("Numero de telefono:" + numeroTelefonico)
    file.write("\n")
    file.write("Correo: " + correo)
    file.write("\n")
    file.write("Provincia: " + provincia)
    file.write("\n")
    file.write("Canton: " + canton)
    file.write("\n")
    file.write("Distrito: " + distrito)
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

def mostrarFactura ():
    file=open("facturaElectronica.txt","r")
    mensaje = file.read()
    print(mensaje)
    file.close()

import random
import string

codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


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
    cobro= input("Ingrese forma de pago Tarjeta o Efectivo: ")
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

    file = open("paquetes.txt","w")
    file.write("\n")    
    file.write("\n")
    file.write("Numero de guia: " + numeroGuia)
    file.write("\n")
    file.write("Destinatario: " + destinatario)
    file.write("\n")
    file.write("Numero de telefono: " + numeroTelefono)
    file.write("\n")
    file.write("Cedula: " + cedula)
    file.write("\n")
    file.write("Peso total del paquete: " + peso + " Kg ")
    file.write("\n")
    file.write("Forma de pago: " + cobro)
    file.write("\n")
    file.write("Monto a cancelar: " + monto +  " colones ")
    file.write("\n")
    file.write("Ubicacion del local: " + ubicacionDelLocal)
    file.write("\n")
    file.write("Estado del paquete: Creado")
    file.write("\n")
    print("La informacion fue grabada correctamente!")
    file.close()

def mostrarPaquetes():
    file = open ("paquetes.txt","r")
    mensaje = file.read()
    print(mensaje)
    file.close()



def estadistica():
    # Leer los datos del archivo 'datosUsuarios.txt'
    with open('datosUsuarios.txt', 'r') as f:
        lineas = f.readlines()

    # Crear un diccionario con los datos
    datos = {}
    for linea in lineas:
        valores = linea.strip().split(': ')
        if len(valores) == 2:
            clave, valor = valores
            datos[clave] = valor
        else:
            print('Error: La línea "{}" no tiene el formato esperado'.format(linea.strip()))

    # Pedir al usuario que ingrese el nombre o la cédula
    clave_busqueda = input('Por favor ingresa el Nombre del dueño o el número de cédula: ')

    # Verificar si la clave de búsqueda está en el diccionario
    if clave_busqueda == datos['Nombre del dueño'] or ('numero de cedula' in datos and clave_busqueda == datos['numero de cedula']):
        print('¡Los datos ingresados son correctos!')

        # Preguntar al usuario qué información desea ver
        opcion = input('¿Qué información desea ver? (Cantidad de envios / Lista de paquetes enviados / Monto a cancelar): ')

        # Verificar la opción seleccionada por el usuario
        if opcion == 'Cantidad de envios':
            cantidad_pedidos = 0
            with open('paquetes.txt', 'r') as f:
                lineas = f.readlines()
                for linea in lineas:
                    if ',' in linea:
                        cedula, cantidad = linea.strip().split(',')
                        if 'numero de cedula' in datos and cedula == datos['numero de cedula']:
                            cantidad_pedidos += int(cantidad)
            print('La cantidad de envios realizados por', datos['numero de cedula'], 'es:', cantidad_pedidos)
        elif opcion == 'Lista de paquetes enviados':
            lista_paquetes_enviados = []
            with open('paquetes.txt', 'r') as f:
                lineas = f.readlines()
                for linea in lineas:
                    if ',' in linea:
                        cedula, cantidad = linea.strip().split(',')
                        if 'numero de cedula' in datos and cedula == datos['numero de cedula']:
                            lista_paquetes_enviados.append(cantidad)
            print('La lista de paquetes enviados por', datos['numero de cedula'], 'es:', lista_paquetes_enviados)
        elif opcion == "Monto a cancelar":
            monto_cobro = 0
            with open('paquetes.txt', 'r') as f:
                lineas = f.readlines()
                for linea in lineas:
                    if ',' in linea:
                        cedula, cantidad = linea.strip().split(',')
                        if 'numero de cedula' in datos and cedula == datos['numero de cedula']:
                            monto_cobro += int(cantidad) * int(paquetes[cantidad]['precio'])
            print('El monto total a cobrar por los paquetes enviados por', datos['numero de cedula'], 'es:',monto_cobro)
        else:
            print('Opción inválida. Por favor ingrese una opción válida.')


    
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
    print("5. Cambiar estado del paquete")
    print("")
    print("6. Rastrear paquete")
    print("")
    print("7. Estadisticas de usuario")
    print("")
    print("8. Salir")
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
        crearPaquete()
        mostrarPaquetes()
        
        
    if opcion == '5':

        print("")
        print("1. En ruta")
        print("")
        print("2. Entregado")
        print("")
        print("3. Entrega Fallida ")
        print("")

        opcion2 = input("Ingrese el estado del paquete: ")

        if opcion2 == '1':
            print("\n")
            print("Se a cambiado el estado del paquete a: \nEn ruta")
            print("\n")
        elif opcion2 == '2':
            print("\n")
            print("Se a cambiado el estado del paquete a: \nEntregado")
            print("\n")
        elif opcion2 == '3':
            print("\n")
            print("Se a cambiado el estado del paquete a: \nEntrega fallida")
            print("\n")
            
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

        opcion4 = opcion2
        
        if opcion4 == "1":
            print("\n")
            print("Su producto está en ruta y contiene la siguiente informacion: ")
            mostrarPaquetes()
            print("\n")
        elif opcion4 == "2":
            print("\n")
            print("Su paquete ha sido entregado. ¡Gracias por su compra!")
            print("\n")
        elif opcion4 == "3":
            print("\n")
            print("Lo sentimos, su entrega ha fallado. Mañana volveremos a procesar el envío. ¡Gracias por su atención!")
            print("\n")

    

    if opcion == '7':
         estadistica()
        
    if opcion == '8':
        break

    
     

    

        
        

       
        

