# Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
jogador = int(input(''' Suas opções:
	[0] PEDRA
	[1] PAPEL
	[2] TESOURA

	'''))
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA')
sleep(1)
print('O computador escolheu', itens[computador])
print('O jogador escolheu', itens[jogador])
print('-=-' * 10)

if jogador == 0: #jogador jogou PEDRA
	if computador == 0:
		print('EMPATE!!!')
	elif computador == 1:
		print('computador VENCEU!!!')
	elif computador == 2:
		print('computador PERDEU!!!')
elif jogador == 1: #jogador jogou PAPEL
	if computador == 1:
		print('EMPATE!!!')
	elif computador == 2:
		print('computador VENCEU!!!')
	elif computador == 0:
		print('computador PERDEU!!!')
else: #jogador jogou TESOURA
	if computador == 2:
		print('EMPATE!!!')
	elif computador == 0:
		print('computador VENCEU!!!')
	else:
		print('computador PERDEU!!!')	