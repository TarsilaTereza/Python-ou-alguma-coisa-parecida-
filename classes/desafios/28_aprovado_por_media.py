#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida
n1 = float(input('Qual sua primeira nota? '))
n2 = float(input('Qual sua segunda nota? '))
m = (n1 + n2)/2
if m >= 6:
	print(
		'Sua nota foi {:.2}, você foi APROVADO!'.format(m))
else:
	print('Sua nota foi {:.2}, você foi REPROVADO!'.format(m))