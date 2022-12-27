# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão. Usando o while dessa vez.
pTermo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão dessa PA: '))
termo = pTermo
c = 1
while c <= 10:
	termo = termo + razao
	c += 1
	print(termo, end = ' ')	