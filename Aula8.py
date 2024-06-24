import time
def somar_dois_numeros():
    numero1 = int(input('Digite um número:'))
    numero2 = int(input('Digite outro número: '))
    print(f'{numero1} + {numero2} =',numero1 + numero2)
def multiplicar_dois_numeros():
    numero1 = int(input('Digite um número:'))
    numero2 = int(input('Digite outro número: '))
    print(f'{numero1} x {numero2} =',numero1 * numero2)
def dividir_dois_numeros():
    numero1 = int(input('Digite um número:'))
    numero2 = int(input('Digite outro número: '))
    print(f'{numero1} / {numero2} =',numero1 / numero2)

print('''
somar [1]
multiplicar [2]
dividir [3]
''')
time.sleep(1)
print('+_+ '*20)
chamar = int(input('Oque quer fazer: '))
if chamar == 1:
    somar_dois_numeros()
elif chamar == 2:
    multiplicar_dois_numeros()
elif chamar == 3:
    dividir_dois_numeros()
else:
    print('Essa operação não existe')
