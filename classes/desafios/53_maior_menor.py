# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
c = num = 0
question = 'Y'
total = []
while question == 'Y':
	num = int(input('Type a number: '))
	question = str(input('Do you want to continue? [Y/N] ')).upper()
	c += 1
	total.append(num)
	mean = sum(total) / len(total)
print('='*35)
print('The mean between the values is {:.2f}, the highest value is {} and the lowest value is {}.'.format(mean, max(total), min(total)))
