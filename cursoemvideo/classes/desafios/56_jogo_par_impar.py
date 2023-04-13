# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
numComp = randint(0, 10)
c = 0
while True:
	numUser = int(input('Type a number: '))
	addition = numUser + numComp
	choiceUser = str(input('Impar ou Par? (I / P) ')).upper()
	if choiceUser == 'P' and addition % 2 == 0:
		print(f'Computer choice {numComp} and user choice {numUser}. The sume between the values is {addition} User winner!!!')
		c += 1
	elif choiceUser == 'I' and addition % 2 != 0:
		c += 1
		print(f'Computer choice {numComp} and user choice {numUser}. The sume between the values is {addition} User winner!!!')
	if choiceUser == 'P' and addition % 2 != 0:
		print(f'Computer choice {numComp} and user choice {numUser}. The sume between the values is {addition} User lost with {c} victories')
		break
	else: 
		print(f'Computer choice {numComp} and user choice {numUser}. The sume between the values is {addition} User winner with {c} victories')
		break
