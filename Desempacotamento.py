def imprimir():
    print('='*50)
    print('='*50)


def pessoa(nome, sobrenome, idade):
    print(nome)
    print(sobrenome)
    print(idade)

tupla = "Edson", "Padilha", 39

imprimir()
pessoa(*tupla)# * faz o desempacotamento de lista e tupla
imprimir()

lista = ["Edson", "Padilha", 39]
pessoa(*lista)
imprimir()
dicionario = {"nome":"Edson", "sobrenome":"Padilha", "idade":19}
pessoa(**dicionario)# Dois ** para desempacotar dicionário
imprimir()
