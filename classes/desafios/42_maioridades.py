# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
for c in range (0, 7):
	ano = int(input('Em que ano você nasceu? '))
	atual = date.today().year - ano