lista = [100, 200, 300, 400]
for item in lista:
    print(item)# Mostra um item da lista de cada vez

lista1 = list(range(4))# Criando lista com range
print(lista1)

lista_num = [100, 200, 300, 400, 500, 600, 700, 800]

for index, item in enumerate (lista_num):# Criando index na lista
    lista_num[index] += 1000 # Operações matemáticas
print(lista_num)

lista_num1 = [150, 250, 350, 450, 550, 650, 750, 850]

for item in range(len(lista_num1)):# Utilizando o Len
    lista_num1[item] += 1000 # Operações matemáticas
print(lista_num1)



