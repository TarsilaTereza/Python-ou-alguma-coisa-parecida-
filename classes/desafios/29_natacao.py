# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

# – Até 9 anos: MIRIM

# – Até 14 anos: INFANTIL

# – Até 19 anos: JÚNIOR

# – Até 25 anos: SÊNIOR

# – Acima de 25 anos: MASTER
nascimento = int(input('Em que ano o competidor nasceu ? '))
from datetime import date
atual = date.today().year
idade = atual - nascimento
if idade <= 9:
	print('Competidor da categoria MIRIM')
elif idade <= 14: 
	print('Competidor da categoria INFANTIL')
elif idade <= 19:
	print('Competidor da categoria JÚNIOR')
elif idade <= 25:
	print('Competidor da categoria SÊNIOR')
else:
	print('Competidor da categoria MASTER')