# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
lista = []
for c in range (1, 6):
	peso = int(input('Qual o seu peso em gramas? '))
	lista.append(peso)
	lista.sort()
print('O maior peso foi {}. O menor foi {}'.format(lista[4], lista[0]))
print(lista)