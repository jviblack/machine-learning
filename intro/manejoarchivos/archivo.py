archivoSalida = open('Salida.txt', 'wt')

archivoSalida.write(str(type(archivoSalida)))

archivoSalida.write("\nHola Archivo")
archivoSalida.write("\nOtra cosa")
texto = "\nMás texto"
archivoSalida.write(texto)
archivoSalida.close()

archivoSalida = open('Salida.txt', 'rt')
print(archivoSalida.read())
archivoSalida.close()
