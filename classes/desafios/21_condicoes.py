#computador escolhe um número de 0 a 5 e o usúario tenta acertar
# from random import randint
# e = randint(0, 5)
# n = float(input('Advinhe o número entre 0 e 5: '))
# if n == e:
# 	print('Você acertou, parabéns! o número escolhido foi {}'.format(e))
# else:
# 	print('Você errou. o número escolhido foi {}'.format(e))

#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite
# v = float(input('Qual a velocidade? '))
# if v > 80:
# 	multa = (v - 80) * 7
# 	print('A velocidade excedeu o limite. a sua multa tem valor de ', multa)

#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
# number = int(input('Escolha um número inteiro: '))
# result = number % 2
# if result == 0:
# 	print('{} é par'.format(number))
# else:
# 	print('{} é impar'.format(number))

#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
d = float(input('Quanto percorreu? '))
if d < 200:
	v = d * 0.5
	print('Sua viagem custou {}'.format(v))
else:
	v = d * 0.45
	print('Sua viagem custou {}'.format(v)) 