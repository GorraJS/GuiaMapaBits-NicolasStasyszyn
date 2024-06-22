from PIL import Image;
from prettytable import PrettyTable
import os

print('Ingrese direccion de imagen:')
localImg = input() #/home/gorra/Escritorio/Gorra/User/Fotos/JoeyJordison.jpg
print()

Imagen = Image.open(f'{localImg}')
cutIMG = os.path.split(localImg)
IMG = cutIMG[1]

fileExten = Imagen.format 
fileResol = Imagen.size
fileCP = Imagen.width * Imagen.height

mytable = PrettyTable(['Nombre','Extension','Resolucion','Cantidad de Pixeles','Ruta'])
mytable.add_row([IMG,fileExten,fileResol,fileCP,localImg])

img = Image.open(localImg)
img.show()
print(mytable)

