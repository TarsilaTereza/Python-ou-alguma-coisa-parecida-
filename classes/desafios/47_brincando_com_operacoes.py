# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
num1 = int(input('Insira um valor: '))
num2 = int(input('Insira um valor: '))
option = 0
print('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
''')
while option != 5:
	option = int(input('Escolha uma opção: '))
	if option == 1:
		print('A SOMA de {} + {} é {}'.format(num1, num2, num1 + num2))
	elif option == 2:
		print('A MULTIPLICAÇÃO de {} x {} é {}'.format(num1, num2, num1 * num2))
	elif option == 3:
		lista = [num1, num2]
		print(max(lista), ' é maior que ' ,min(lista))
	elif option == 4:
		num1 = int(input('Insira um valor: '))
		num2 = int(input('Insira um valor: '))
	elif option == 5:
		print('Acabou')
	else:
		print('Valor inválido')
print('Volte sempre')