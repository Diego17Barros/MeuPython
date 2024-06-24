print('''Imprimindo um retângulo 
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
@@@@@@
''')

linha = 6
colunas = 6
simbolo = '01'
for l in range(linha):
    for c in range(colunas):
        print(simbolo, end= '')
    print()