#La clase B hereda los método y atributos de la clase A

class ClaseA:
    def __init__(self, x):
        self.a = x
        self.b = 2*x
    
    def muestra(self):
        print("a=%i, b=%i" % (self.a, self.b))

class ClaseB(ClaseA):
    def __init__(self, x, y):
        ClaseA.__init__(self, x)
        self.c = 3 * (x + y) + self.b
    def muestra(self):
        print("a=%i, b=%i, c=%i" % (self.a, self.b, self.c))

#Muestra los atributos de la clase
print("objeto A")
a = ClaseA(2)
print(a.__dict__)
a.muestra()

print("objeto B")
b = ClaseB(2, 3)
print(b.__dict__)
b.muestra()