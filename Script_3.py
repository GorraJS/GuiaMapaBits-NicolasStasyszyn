from PIL import Image
import os

print('Ingrese ruta del archivo:')
routeFile = input() #/home/gorra/Escritorio/Gorra/ITR/Programacion/Python/Guia_4/Fotos/GibsonGuitar.jpg
print('Ingrese los grados de rotacion:')
grados = int(input())

img = Image.open(f'{routeFile}')
rotatedImage = img.rotate(grados)
rotatedImage.show()

routeFileCut = os.path.split(routeFile)
file = routeFileCut[1]
saveRoute = routeFileCut[0]
rotatedImage.save(f'{saveRoute}/Copy-{file}')