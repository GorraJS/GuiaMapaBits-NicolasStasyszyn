from PIL import Image
import os

print('Ingrese ruta de la imagen:')
fileRoute = input() #/home/gorra/Escritorio/Gorra/ITR/Programacion/Python/Guia_4/Fotos/JoeyJordison.jpg

print('Ingrese ruta de la marca de agua:')
markRoute = input() #/home/gorra/Escritorio/Gorra/ITR/Programacion/Python/Guia_4/Fotos/MA/MarcaDeAgua.jpg

print('Ingrese ubicacion de la marca de agua')
print('[Superior Izquierda(SI) - Inferior Izquierda(II) - Superior Derecha(SD) - Inferior Derecha(ID)]')
posicion = input()


openFile = Image.open(f'{fileRoute}')
openMark = Image.open(f'{markRoute}')

copyFile = openFile.copy()
copyMark = openMark.copy()

resFile = openFile.size
resMark = openMark.size

if posicion == 'Superior Izquierda' or posicion == 'superior izquierda' or posicion == 'si' or posicion == 'SI':
    copyFile.paste(copyMark,(0,0))
    
elif posicion == 'Inferior Izquierda' or posicion == 'inferior izquierda' or posicion == 'ii' or posicion == 'II':
    copyFile.paste(copyMark,(0,resFile[1]-resMark[1]))
    
elif posicion == 'Superior Derecha' or posicion == 'superior derecha' or posicion == 'sd' or posicion == 'SD':
    copyFile.paste(copyMark,(resFile[0]-resMark[0],0))
    
elif posicion == 'Inferior Derecha' or posicion == 'inferior derecha' or posicion == 'id' or posicion == 'ID':
    copyFile.paste(copyMark,(resFile[0]-resMark[0],resFile[1]-resMark[1]))

routeCut = os.path.split(f'{fileRoute}')
nameFile = 'MarcaDeAgua' + routeCut[1]
copyFile.show()
copyFile.save(f'Fotos/{nameFile}')