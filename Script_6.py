from PIL import Image
import os

print("Ingrese ruta del archivo:")
fileRoute = input()  # /home/gorra/Escritorio/Gorra/ITR/Programacion/Python/Guia_4/Fotos/act6-9FOTOS

print("Ingrese resolucion en X:")
resX = str(input())  # .1500

print("Ingrese resolucion en Y:")
resY = input()  # .1500

canvasRes = (resX, resY)

contenido = os.listdir(fileRoute)

files = None
for elem in os.walk(fileRoute):
    files = elem[2]


resFileX = 500
resFileY = 500


def reSize(files):
    
