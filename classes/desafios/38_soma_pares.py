# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
lista = []
for c in range(0, 6):
	num = int(input('Escolha um valor: '))
	if num % 2 == 0:
		lista.append(num) # adiciona os valores pares na lista 'lista' :)
		soma += num
print('a soma entre {} é {}'.format(lista, soma))