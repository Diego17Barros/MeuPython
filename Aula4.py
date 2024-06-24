from random import randint
n = randint(0, 10)
for n in range(5):
    n = int(input('Digite o número correto: '))
    print('Adivinhe em que número a máquina está pensando de 0 a 10')
else:
    print('Meus parabéns você acertou!!!')
