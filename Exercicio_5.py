# Faça um algoritimo que peça a idade do usuário e a idade de sua mãe. Em seguida, imprima na tela com quantos anos sua mãe o teve. 

idade = int(input('Digite sua idade: '))
mae = int(input('Idade de sua mãe: '))

resultado = mae - idade

if  resultado <= 14:
    print('Verifique os dados de entrada!!!')

else:
    resultado < 14
    print(f'Sua mãe teve você com {resultado} anos de idade.')