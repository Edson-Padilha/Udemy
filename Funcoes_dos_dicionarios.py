tel = {}
tel = {}
print()
tel = {30301122: "Pericles",
       33547877: "Menelau",
       33381245: "Atreu",
       36458899: "Tieste"
       }
print(tel)
print()
print(len(tel))# Conta quantidade de elementos do dicionário
del(tel[36458899])# Exclui elemento do dicionário
print(tel)
print(tel.keys())# Imprime a lista de chaves)
print()
print(tel.values())# Imprime lista dos valores
print()
print(tel.get(30301122))
print()
print(tel.popitem())# Retorna um elemento aleatório e remove da lista
print()

if 33547877 in tel:# Verifica se numero está dentro do dicionário
    print('Telefone cadastrado')
else:
    print('Não cadastrado.')
print()
print('Mesclar dicionário')
tel2 = {99999999: "teste1", 55551111: "teste2"}
print(tel2)
print()
tel.update(tel2)# Coloca os elementos do dic
print(tel)
