# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.

adult = men = youngWomen = 0
while True:
	name = str(input('Nome: '))
	sex = str(input('Gênero[M/f] : ')).upper()
	age = int(input('Idade: '))
	question = str(input('Quer cadastrar outra pessoa? [S/N] ')).upper()
	if question == 'N': #funcionando
		break #funcionando
	elif age > 18:
		adult += 1
	elif 'M' in sex:
		men += 1
	elif sex == 'F' and age < 20:
		youngWomen += 1
print(f'{adult} têm mais de 18 anos, {men} homens foram cadastrados, {youngWomen} mulheres têm menos de 20 anos.')
	
