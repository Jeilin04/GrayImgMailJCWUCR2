import unittest
import os
import requests
from PIL import Image
from urllib.parse import urlparse

os.system('cls') 

class TestImagenesCorreo(unittest.TestCase):

    def test_downloadImage(self):

        url = "https://images.pexels.com/photos/259881/pexels-photo-259881.jpeg?cs=srgb&dl=pexels-pixabay-259881.jpg&fm=jpg"
        funcion_parse = urlparse(url)
        validacion = all([funcion_parse.scheme, funcion_parse.netloc])       
        self.assertTrue(validacion, f"'{url}' no es una URL válida")

    def test_showImage(self):

        URL = "https://images.pexels.com/photos/259881/pexels-photo-259881.jpeg?cs=srgb&dl=pexels-pixabay-259881.jpg&fm=jpg"
        response = requests.get( URL)
        self.assertTrue(response.headers.get("content-type").startswith("image/"))

    def test_grayScale(self):

        ruta = "C:/CursoPythonGit/Pythonnivel1/Nivel_2/1_Tareas/Proyecto/test/imagen_b.jpg"
        with Image.open(ruta) as img:
            self.assertTrue(img.mode in ('L', '1'))

    def test_Mail(self):

        CorreoValido = "correo@gmail.com"  
        self.assertTrue("@" in CorreoValido, f"'{CorreoValido}' correo inválido no contiene @ ")

    def test_Mail2(self):

        Asunto = "Prueba Unitaria"  
        self.assertTrue(Asunto, "No tiene asunto")


if __name__ == "__main__":
    unittest.main()

