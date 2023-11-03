archivo = open('Salida.txt', 'rt')

archivo.seek(20) #Salta a la posición 20 dento del texto
print(archivo.read())

archivo.seek(0) #Vuelve a la posición 0

print(archivo.read(40))
print(archivo.read())

print(archivo.tell()) #Devuelve la posición del último caracter
archivo.close()