#Llenar la tabla con for mediante x.format(x, x*x, x*x*x)
for x in range(1, 15):
    print('{0:4d}{1:5d}{2:6d}'.format(x, x*x, x*x*x))
    #Cada elemento entre llaves es una columna asignada a un orden .format()
    #{0:2d} deja la tabla con espacio suficiente para verse bien