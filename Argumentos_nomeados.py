def imprimir():
    print('='*50)
    print('='*50)


def argumentos(nome, sobrenome, idade, sexo):
    print(f' Nome: {nome}\n',f'Sobrenome: {sobrenome}\n',f'Idade: {idade}\n',f'Sexo: {sexo}\n')


def nomeados(nome, sobrenome, idade, sexo):
    print(f' Nome:{nome}\n', f'Sobrenome:{sobrenome}\n',f'Idade: {idade}\n',f'Sexo: {sexo}')

imprimir()
argumentos("Edson", "Padilha", 39, True)

imprimir()

nomeados( nome = " Marciano ", sobrenome = " Rodrigues", idade = 39, sexo = True )

imprimir()