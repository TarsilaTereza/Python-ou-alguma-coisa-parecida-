# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
totMaior = 0
totMenor = 0
for pess in range(1, 8):
	nasc = int(input('Em que ano você nasceu? '))
	atual = date.today().year - nasc
	if atual >= 21:
		totMaior += 1
	else:
		totMenor += 1
print('Ao tivemos {} menores e {} maiores'.format(totMenor, totMaior))