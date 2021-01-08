# Faça um algoritmo que peça dois números. Primeiro, imprima o maior e, em seguida, o menor.

num = int(input('Digite número: '))
num1 = int(input('Segundo número: '))

maior = max(num, num1)
menor = min(num , num1)

print('='*20)
print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')
print('='*20)