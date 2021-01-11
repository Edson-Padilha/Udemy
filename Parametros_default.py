def imprimir():
    print('='*50)

def login(sistema= '01', usuario= 'root', senha= '1234'):
    print('Usuário: ',usuario)
    print('Senha: ', senha)
    print('Empresa: ', sistema)
imprimir()
login("01", "root", "1234")
imprimir()