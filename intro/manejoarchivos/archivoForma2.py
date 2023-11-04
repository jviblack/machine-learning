texto = "\nHola Archivo"
archivo = open ('Archivo.txt', 'wt')
archivo.write(texto)
texto = "\nPrueba"
archivo.write(texto)
texto = "\nLínea 1"
archivo.write(texto)
texto = "\nLínea 2"
archivo.write(texto)
archivo.close()

with open ("archivo.txt", "rt") as archivo:
    print(archivo.read())

archivo.close()