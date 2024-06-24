def login():
    nome = str(input('Digite seu nome: '))
    email = str(input('Digite seu email: '))
    senha = str(input('Digite sua senha: '))
    senha_correta = 'Diego10'
    if senha == senha_correta:
        print(f'Bem vindo, {nome}')
    else:
        print('Senha incorreta, tente novamente')
login()