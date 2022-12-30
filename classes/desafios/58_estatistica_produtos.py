# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.

# B) quantos produtos custam mais de R$1000.

# C) qual é o nome do produto mais barato.
total = expensive = 0
products = []
values = []
while True:
	name = str(input('Nome do produto: '))
	price = float(input('Preço: '))
	question = str(input('Deseja adicionar mais produtos? [S/N] ')).strip().upper()[0]
	total += price #soma todos os preços
	if question == 'N':
		break
	if price > 1000:
		 expensive += 1
	products.append(name)
	values.append(price)
	position = values.index(min(values))
print(f'O preço total foi de R$ {total}')
print(f'{expensive} produtos custam mais de R$ 1000,00')
print(f'O menor produto comprado foi {products[position]}')