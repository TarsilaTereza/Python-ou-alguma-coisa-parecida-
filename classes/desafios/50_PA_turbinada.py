# Melhore o DESAFIO 49, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
pTermo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão dessa PA: '))
termo = pTermo
c = 1
while c <= 10:
	termo = termo + razao
	c += 1
	print(termo, end = ' ')
mais = int(input('Quantos termos você quer mostrar a mais? '))
adicionado = 1
print('=-=' * 10)
if mais == 0:
	print('Obrigada por usar a PA turbinada!')
elif mais > 0:
	while adicionado <= mais:
		adicionado += 1
		termo += razao
		print(termo, end = '->')	
else:
	print('Valor inválida. Escolha um valor maior que 0')