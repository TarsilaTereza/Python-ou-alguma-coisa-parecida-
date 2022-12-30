# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.

# B) quantos homens foram cadastrados.

# C) quantas mulheres tem menos de 20 anos.
c = youngWomen = 0
while True:
	adult = 0
	men = 0
	name = str(input('Qual seu nome? '))
	age = int(input('Qual sua idade? '))
	sex = str(input('Qual seu gênero? [M/F] ')).upper()
	question = str(input('Deseja cadastrar mais pessoas? [S/N] ')).upper()
	if 'N' in question:
		break
	elif 'M' in sex:
		men += 1
	elif age > 18:
		adult += 1
	elif 'F' in sex and age < 20:
		youngWomen += 1 #funcionando
print(f'{adult} pessoas tem mais de 18 anos, {men} homens foram cadastrados e {youngWomen} mulheres tem menos de 20 anos.')