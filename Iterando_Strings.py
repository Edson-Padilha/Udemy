print('---- Exemplo 1')
print()
s = 'Iterando Strings'
for c in s:
    print(c)
    print()
print('---- Exemplo 2')
print()
s = 'Iterando Strings'
indice = 0
while indice < len(s):
    print(indice,s[indice])
    indice += 1


print('---- Exemplo 3')
print()

for k,v in enumerate ('Iterando Strings'): 
    print(k, v)
print()

