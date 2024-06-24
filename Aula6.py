oque = str(input('Em qual seção se encaixa o seu produto: ')).upper().strip()
item = str(input('Qual seu item: ')).capitalize()
peso = int(input('Qual o peso desse item em gramas: '))
marca = str(input('Qual a marca desse item: ')).capitalize()
preco = float(input('Qual o preço desse item: '))
print('-=-='*15)
data = int(input('Qual o dia de vencimento desse produto: '))
data1 = int(input('Qual o mês de vencimento desse produto: '))
data2 = int(input('Qual o ano de vencimento desse produto: '))
if oque == 'FRUTAS':
    print(f'Frutas- {item}, Peso = {peso}g, Marca: {marca}, R${preco}, {data}/{data1}/{data2}')
if oque == 'VERDURAS':
    print(f'Verduras- {item}, Peso = {peso}g, Marca: {marca}, R${preco}, {data}/{data1}/{data2}')
if oque == 'AÇOUGUE':
    print(f'Açougue- {item}, Peso = {peso}g, Marca: {marca}, R${preco}, {data}/{data1}/{data2}')
if oque == 'LIMPEZA':
    print(f'Límpeza- {item}, Peso = {peso}g, Marca: {marca}, R${preco}, {data}/{data1}/{data2}')
if oque == 'FRIOS':
    print(f'Frios- {item}, Peso = {peso}g, Marca: {marca}, R${preco}, {data}/{data1}/{data2} ')
else:
    print('Esse produto não está em estoque nesse mercado')
