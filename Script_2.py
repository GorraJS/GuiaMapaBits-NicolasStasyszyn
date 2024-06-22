from PIL import Image
import os, requests

ruta = 'Fotos/korn.jpg'
img = Image.open(f'{ruta}')
img.show()

rutaFile= os.path.split(ruta)
nameFile = rutaFile[1]
rutaCarpeta = rutaFile[0]
img.save(f'{rutaCarpeta}/copy-{nameFile}')