#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
idade = atual - ano
if idade > 18:
	print('Já deveria ter se alistado')
elif idade == 18:
	print('Deve se alistar imediatamente')
else:
	print('Faltam {} para se alistar'.format(18-idade))