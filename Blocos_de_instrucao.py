num1 = int(input('Digite um numero: '))

if (num1 > 10):
    print('O valor é maior que 10!')

    if (num1 < 15):
        print('O numero é maior que 10 e menor que 15!')

    else:
        if(num1 <= 50):
            print('O valor é maior que 10 e menor ou igual a 50!')

        else:
            print('O valor é maior que 50!')

else:
    if(num1 > 5):
        print('O numero é menor que 10 e maior que 5!')

        if (num1 == 7):
            print('O numero é igual a 7!')

    else:
        print('O valor é menor que 5!')