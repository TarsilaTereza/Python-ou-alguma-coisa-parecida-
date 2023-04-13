# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
value = int(input('Qual o valor que você quer sacar? '))
total = value
ballot = 50
totalBallot = 0
while True:
	if total >= ballot:
		total -= ballot
		totalBallot += 1
	else:
		if totalBallot > 0:
			print(f'Total de {totalBallot} cédulas de R$ {ballot}')
		if ballot == 50:
			ballot == 20
		elif ballot == 20:
			ballot == 10
		elif ballot == 10:
			ballot == 1
		if total == 0:
			break
print('*'*50)

