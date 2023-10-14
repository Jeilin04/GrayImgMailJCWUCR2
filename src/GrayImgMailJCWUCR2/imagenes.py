import os
import requests
from PIL import Image
from PIL import ImageOps
from io import BytesIO

os.system('cls') 

print("¡Bienvenido! A continuación se descargará una imagen de internet, se mostrará en pantalla y se guardará en una carpeta la versión gris de dicha imagen \n")

#Variables necesarias y llamado de funciones de imágenes
URL = "https://images.pexels.com/photos/259881/pexels-photo-259881.jpeg?cs=srgb&dl=pexels-pixabay-259881.jpg&fm=jpg"
rutaPC = input("¡Favor digite la ruta en la que desea almacenar la imagen descargada!\n(Ejm ---> C:/CursoPythonGit/Pythonnivel1/Nivel_2/1_Tareas/ProyFinal) \n\n")

#Rutas para imagen 
ruta_completa = os.path.join(rutaPC, f"imagen_a.jpg")

def showImageFromURL(url:str): 

    """
    |
    
    Descarga una imagen desde una URL y la muestra
    
    **Argumentos:**

    :url(str): Ruta de la URL de la imagene deseada

    """

    mostrar = requests.get(url)
    with Image.open(BytesIO(mostrar.content)) as mi_imagen:
        mi_imagen.show()
    print("OK")

showImageFromURL(URL)

def downloadImageFromUrl(url:str, path:str):

    """

    Descarga una imagen y la guarda en la ruta indicada
    
    **Argumentos:**

    :url(str): Ruta de la URL de la imagene deseada
    :path(str): Recibe información de una variable que utiliza *os.path.join* para unir la ruta en escritorio donde se guardará el archivo + nombre del archivo para almacenarlo

    **Adicionales:**
    
    Ruta imagen de referencia:
    <https://images.pexels.com/photos/259881/pexels-photo-259881.jpeg?cs=srgb&dl=pexels-pixabay-259881.jpg&fm=jpg>

    Descargable de `Imagen muestra`_.

    .. _Imagen muestra: https://images.pexels.com/photos/259881/pexels-photo-259881.jpeg?cs=srgb&dl=pexels-pixabay-259881.jpg&fm=jpg

    .. image:: https://images.pexels.com/photos/259881/pexels-photo-259881.jpeg?cs=srgb&dl=pexels-pixabay-259881.jpg&fm=jpg

    """
    guardar = requests.get(url)
    with open(path, "wb") as archivo:
        archivo.write(guardar.content)
    print("OK")

downloadImageFromUrl(URL, ruta_completa)

def grayScaleImage(path:str):

    """
    |

    Convierte una imagen a blanco y negro
    
    **Argumentos:**

    :path(str): Recibe información de una variable que utiliza *os.path.join* para unir la ruta en escritorio donde se guardó el archivo + nombre del archivo almacenado

    """
    img_gray1 = Image.open(path)
    img_gray2 = ImageOps.grayscale(img_gray1)
    img_gray2.save(path)  
    print("OK")
   
grayScaleImage(ruta_completa)


