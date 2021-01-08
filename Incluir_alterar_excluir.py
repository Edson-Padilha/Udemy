l = ['bbb', 'ccc', 'ddd']
print(l)
print(l[0])
print(l[1])

l.append('eee')# Inserindo na ultima posição
print(l)

l.insert(0, 'aaa')# Inserindo elemento por posição
print(l)

l [1] = 'rrr'# Alterando elemento na lista
print(l)

l.pop()#Apaga o ultimo elemento da lista
print(l)

l.pop(0)# Escolhe a posição do item excluido
print(l)

del (l[2:4])#Exclui por intervalo
print(l)

l.clear()# Apaga todos os elementos
print(l)
