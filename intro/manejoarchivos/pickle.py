import pickle #Crea representaciones serializadas portables de objetos

lista = ['casa', 'coche', 'manzana', 2+3j, 4]
#Cambiar wt por wb
archivo = open ('archivopickle.txt', 'wb')

pickle.dump(lista, archivo)
archivo.close()

#Leer y cargar contenido del archivo
archivo = open ('archivopickle.txt', 'rb')
cargarLista = pickle.load(archivo)
print(cargarLista)
archivo.close()
