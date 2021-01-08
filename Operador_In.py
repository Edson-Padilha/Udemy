a = 10
b = 25
c = 66

x = int(input('Digite um numero: '))

#if (x == a or x == b or x == c):
    #print('Está contido.')
#else:
    #print('Não está contido.')

if (x in [a,b,c]):# Forma mais elegante
    print('Está contido.')
else:
    print('Não está contido.')

cores = ['azul', 'amarelo', 'vermelho', 'branco']
while True:

    cor = input('Digite o nome e uma cor ou então,\n0 para sair do programa: ')
    if (cor == '0'):
        break
    elif cor in cores:
        print('Essa cor está contida.')
    else:
        print('Essa cor não está contida.')
    print()