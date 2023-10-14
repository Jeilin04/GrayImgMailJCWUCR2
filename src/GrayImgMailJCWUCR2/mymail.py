import os
import threading
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

os.system('cls') 

print("A continuación se enviará por correo la imagen modificada, también se generará un QuickMail de confirmación. ¡Favor brindar los siguientes datos: \n")

#Variables necesarias para email
DatosRemitente = input("Su nombre y apellido \n") #"Jeilin Crawford" 
Correo = input("Su correo \n") 
Contraseña = input("Su contraseña de aplicación \n") 
CorreoReceptor = input("El correo al que desea enciar el archivo \n") #"jeilinj@gmail.com"

rutaPC = input("¡Favor validar la ruta de la imagen descargada!\n(Ejm ---> C:/CursoPythonGit/Pythonnivel1/Nivel_2/1_Tareas/ProyFinal) \n\n")

#Rutas para imagen 
ruta_completa = os.path.join(rutaPC, f"imagen_a.jpg")

def sendQuickMail(subject:str, message:str, destination:str):
    
    """
    |

    Envía un correo electrónico rápido al destino indicado.

    **Argumentos:** 

    :subject(str): Recibe un *Asunto*
    :message(str): Recibe un mensaje para el cuerpo del correo
    :destination(str): Recibe el destino deseado para el correo (receptor)

    """

    #Recibe los parámetros indicados del correo (Título, remitente, receptor...)
    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = subject 
    mensaje["From"] = DatosRemitente 
    mensaje["To"] =  destination    

    #Genera mensaje en cuerpo del correo
    mensajeU = MIMEText(message, "plain")
    mensaje.attach(mensajeU)
    
    #Inicializa TLS, pasa parámetro de usuario y envia email
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as conexion:
        conexion.starttls(context=context)
        conexion.login(Correo, Contraseña) 
        conexion.sendmail(
            Correo, 
            destination,      
            mensaje.as_string()
            )

MensajeUsuario1 = "Se creo imagen deseada en la carpeta"

def sendAttachEmail(subject:str, message:str, destination:str, path:str):

    
    """
    |

    Envía un correo con un archivo adjunto, a la dirección indicada
    
    **Argumentos:**    

    :subject(str): Recibe un *Asunto*
    :message(str): Recibe un mensaje para el cuerpo del correo
    :destination(str): Recibe el destino deseado para el correo (receptor)
    :path(str): Recibe información de una variable que utiliza *os.path.join* con la ruta en escritorio donde se guardó el archivo + nombre del archivo almacenado
    
    """

    #Recibe los parámetros indicados del correo (Título, remitente, receptor...)
    mensaje = MIMEMultipart("alternative")
    mensaje["Subject"] = subject 
    mensaje["From"] = DatosRemitente
    mensaje["To"] =  destination 

    #Abre la imagen con read binary y la adjunta al correo 
    with open(path, "rb") as img:
        image_dato = img.read()
        ArchivoImg = MIMEImage(image_dato, name=os.path.basename(path))
        mensaje.attach(ArchivoImg )

    #Genera mensaje en cuerpo del correo
    mensajeU = MIMEText(message, "plain")
    mensaje.attach(mensajeU)
    
    #Inicializa TLS, pasa parámetro de usuario y envia email
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp.gmail.com", 587) as conexion:
        conexion.starttls(context=context)
        conexion.login(Correo, Contraseña) 

        conexion.sendmail(
            Correo, 
            destination,      
            mensaje.as_string()
            )
        print("\n")

MensajeUsuario2 = "Versión gris de imagen descargada de internet" 

hilo1 = threading.Thread(target=sendQuickMail, args=("QuickMail-Comprobación", MensajeUsuario1, CorreoReceptor))
hilo2 = threading.Thread(target=sendAttachEmail, args=("Imagen Gris de URL", MensajeUsuario2, CorreoReceptor, ruta_completa))
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()

print("Se generó un QuickMail de confirmación")
print("--------------------------------------- \n")
print("Se generó un correo con el adjunto de la imagen generada")
print("--------------------------------------------------------- \n")
