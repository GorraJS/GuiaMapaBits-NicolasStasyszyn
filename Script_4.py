from PIL import Image
import os

print('Escriba ruta de la imagen:')
routeFile = input()  #/home/gorra/Escritorio/Gorra/ITR/Programacion/Python/Guia_4/Fotos/JoeyJordison.jpg

img = Image.open(routeFile)

print('Escriba coordenada inicial')
print('Origen en X')    
xOrigin = int(input())
print('Origen en Y')
yOrigin = int(input())

print('Asigne ancho:')
Ancho = int(input())

print('Asigne largo:')
Largo = int(input())

cordenadas = (xOrigin, yOrigin, xOrigin + Ancho, yOrigin + Largo)

cropImg = img.crop(cordenadas)

cropImg.show()

cutRoute = os.path.split(f'{routeFile}')
nameFile = 'Cropped' + cutRoute[1]
route = cutRoute[0]
os.makedirs('Fotos/Recortes', exist_ok=True)
cropImg.save(f'{route}/Recortes/{nameFile}')