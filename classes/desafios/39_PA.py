# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
pTermo = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão da P.A.: '))
dTermo = pTermo + (10 -1) * razao #décimo termo de uma P.A.
for c in range (pTermo, dTermo + razao, razao):
	print(c, end = '-> ')
print('ACABOU')