# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
n = input('Informe um número ')
num = str(n)
l = list(num)
print('analisando o número {} ...'.format(num))
print('unidade {}'.format(l[-1]))
print('dezena {}'.format(l[-2]))
print('centena {}'.format(l[-3]))