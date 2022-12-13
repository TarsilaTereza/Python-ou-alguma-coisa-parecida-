#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))
lista = [n1, n2, n3] #adiciona os valores em uma lista
print(sorted(lista)) #coloca a lista em ordem crescente
print('O maior número é {}, e o menor é {}'.format(sorted(lista)[-1], sorted(lista)[0]))

#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
s = float(input('Qual seu salário? '))
if s > 1250:
	aumento = s / 10
	print('Você terá um aumento de {} reais. Seu salário passará a ser {}'.format(aumento, aumento+s))