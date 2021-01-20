

def imprimir():
    print('-'*50)
    print('-'*50)


imprimir()


class Retangulo:

    def __init__(self):
        self.a = 0
        self.b = 0

    def area(self):
        return self.a * self.b

r1 = Retangulo()
r2 = Retangulo()

print(r1.area())