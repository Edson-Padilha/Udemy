print('Antes de entrar no laço')
for i in range(10):
    print(i)
    if(i == 6):
        print('A condição estabelecida retornou True')
        break
print('Depois de ter entrado no laço')

i = 10
while(i < 100):
    i += 1
    print(i)
    if(i == 7):
        break