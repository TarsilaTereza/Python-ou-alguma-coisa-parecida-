#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8 (somar os dois termos anteriores)
num = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('-'*30)
print(t1, '->', t2, end = '')
c = 3 #já contou 3 números da sequência até aqui
while c <= num:
	t3 = t1 + t2
	c += 1
	t1 = t2
	t2 = t3
	print( '->', t3, end = ' ')
print('FIM')