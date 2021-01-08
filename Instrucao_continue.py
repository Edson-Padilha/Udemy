for i in range(10):
    if (i == 6):
        continue
    print(i)

print('Inicio')

i = 0
while(i<10):
    i += 1
    if (i % 2 == 0):
        continue
    print(i)
else:
    print('else')
print('Fim')
print()
