acao = int(input("Digite '1' para sim e digite '2' para não: "))
if (acao == 1):
    print("Você disse que sim!")    
elif(acao >2):
    print("Somente os valores 1 e 2 serão aceitos!")
else:
    if (acao==2):
        print("Você disse que não!")
    else:
        print("Somente numeros inteiros 1 e 2! Programa finalizado...")