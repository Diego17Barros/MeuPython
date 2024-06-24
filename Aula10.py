def agencia_volks():
    nome = str(input('Qual seu nome: '))
    print(f'Bem vindo a Volkswagen, {nome}')
    modelo = str(input('Qual o modelo do seu carro: '))
    cor = str(input('Qual a cor do seu carro: '))
    motor = str(input('Qual o motor do seu carro: '))
    preco = float(input('Qual o preço do seu carro: '))
    print(f'''Modelo-{modelo}
    Cor-{cor}
    Motor-{motor}
    Preço-R${preco}
''')
def agencia_fiat():
    nome = str(input('Qual seu nome: '))
    print(f'Bem vindo a Fiat, {nome}')
    modelo = str(input('Qual o modelo do seu carro: '))
    cor = str(input('Qual a cor do seu carro: '))
    motor = str(input('Qual o motor do seu carro: '))
    preco = float(input('Qual o preço do seu carro: '))
    print(f'''Modelo-{modelo}
Cor-{cor}
Motor-{motor}
Preço-R${preco}
''')



print('''Volkswagen[1]
Fiat[2]
''')
chamar = int(input('Qual agência gostaria de ver: '))
if chamar == 1:
    agencia_volks()
elif chamar == 2:
    agencia_fiat()
else:
    print('Nós não temos essa agência')
