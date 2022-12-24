# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
youngWomen = []
oldMan = []
sume_age = 0
from datetime import date
for c in range(1, 5):
	name = input('Nome: ')
	age = int(input('Idade: '))
	sume_age += age # para a média
	sex = input('Sexo [M / F]: ')
	if sex == 'F' and age < 20:
		youngWomen.append(name) #lenth
	elif sex == 'M':
		oldMan.append(name)
		oldest = min(oldMan)
if len(youngWomen) > 1:
	print('A média da idade do grupo é de {} anos, o homem mais velho é {} e {} mulheres têm menos de 20 anos'.format(sume_age / 4, oldest, len(youngWomen)))
else:	
	print('A média da idade do grupo é de {} anos, o homem mais velho é {} e {} mulher tem menos de 20 anos'.format(sume_age / 4, oldest, len(youngWomen)))
