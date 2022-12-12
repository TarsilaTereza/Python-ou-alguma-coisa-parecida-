#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
s = float(input('Qual seu salário? '))
if s > 1250:
	aumento = s / 10
	print('Você terá um aumento de R$ {}. Seu salário passará a ser R$ {}'.format(aumento, aumento+s))
else:
	aumento = (s * 15) / 100
	print('Você terá um aumento de R$ {}. Seu salário passará a ser R$ {}'.format(aumento, aumento+s))

#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite um valor: '))
v3 = int(input('Digite um valor: '))
if v1 > v2 + v3 or v2 > v1 + v3 or v3 > v1 + v2:
	print('Isso não é um triângulo')
else:
	print('Isso é um triângulo')