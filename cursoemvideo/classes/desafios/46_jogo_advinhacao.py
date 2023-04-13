# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer
from random import randint
numComp = randint(0, 10)
c = 1
while True:
	numUser = int(input('Digite um número entre 0 e 10: '))
	if 0 <= numUser <= 10:
		if numUser == numComp:
			print('Parabéns, você acertou! O número escolhido pelo computador foi {}, você precisou de {} tentativas para acertar'.format(numComp, c))
		else:
			numUser = int(input('Você errou, tente novamente: '))
			c += 1 #adiciona mais uma tentativa ao contador
	else:
		print('Valor inválido. Digite um número entre 0 e 10: ')