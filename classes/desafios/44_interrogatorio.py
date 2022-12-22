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
		oldest = max(oldMan)
print('A média da idade do grupo é {}, o homem mais velho é {} e {} mulheres tem menos de 20 anos'.format(sume_age / 2, oldest, len(youngWomen)))	
print(len(youngWomen))
print(youngWomen)