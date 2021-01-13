def imprimir():
    print('='*50)
    print('='*50)

lista = [11, 10, 14]

def func(a, b, c):
    print(a)
    print(b)
    print(c)

imprimir()

lista.sort() # Ordena em ordem crescente

func(*lista)

imprimir()

func(**dict(zip(("b", "a", "c"), lista)))
