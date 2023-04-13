# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
# número primo = maior que um e divisível por 1 e por ele mesmo
num = int(input('Digite um número: '))
divisao = 0 
print('=' * 40)
for c in range (1, num + 1):
	if num % c == 0:
		print('\033[34m', end = ' ') #amarelo
		divisao += 1
	else:
		print('\033[31m', end = ' ') #vermelho
	print(c, end = ' ')
# print('=' * 40)
print('''
\033[mO número {} foi dividido {} vezes.'''.format(num, divisao))
if divisao > 2:
	print('{} não é ímpar'.format(num))
else:	
	print('{} é ímpar'.format(num))	
