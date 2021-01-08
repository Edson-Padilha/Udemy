idade = int(input("Informe a sua idade: "))
if(idade<=0):
    print("A sua idade não pode ser menor que 0")
elif(idade>=150):
    print("Sua idade não pode ser maior que 150 anos.")
elif(idade<=18):
    print("Você precisa ter 18 anos.")
else:
    print("Idade aceita!!!")