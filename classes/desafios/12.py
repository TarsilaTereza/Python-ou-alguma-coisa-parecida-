#  Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

# MODO 1
n = float(input('Digite um número: '))
print('A parte inteira de {} é {}'.format(n, int(n)))

#MODO 2
from math import trunc # trunc quebra o número e mostra a parte inteira
n = float(input('Digite um número: '))
print('A parte inteira de {} é {}'.format(n, trunc(n)))

