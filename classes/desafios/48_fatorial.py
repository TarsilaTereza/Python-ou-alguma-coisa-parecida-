# Faça um programa que leia um número qualquer e mostre o seu fatorial.
num = int(input('Digite um número: '))
c = num #o contador vai ser o próprio número
f = 1
while c > 0:
	print(' {} '.format(c), end = '')
	print('x' if c > 1 else '= ', end = '')
	f = f * c
	c -= 1
print(f)