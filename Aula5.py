valor = int(input('Digite o valor do seu produto: '))
while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto é de R${valor}')
    break


