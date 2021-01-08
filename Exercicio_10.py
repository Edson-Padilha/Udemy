#Faça um algoritmo que verifica se um determinado valor é uma String

entrada = input('Digite alguma coisa: ')

if type(entrada) == int:
    print('Número inteiro')
elif type(entrada) == float:
    print('Número decimal')
else:
    type(entrada) == str
    print('É uma string.')
