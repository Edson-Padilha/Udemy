def imprimir():
    print('='*50)
    print('='*50)


def potencia(x):
    quadrada = x**2
    cubo = x**3

    return quadrada, cubo

imprimir()

q,c = potencia(10)

print(q)
print(c)

imprimir()