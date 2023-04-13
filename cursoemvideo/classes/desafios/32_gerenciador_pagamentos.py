# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço formal 

# – 3x ou mais no cartão: 20% de juros
pNormal = float(input('Qual o valor do produto? '))
print(''' Temos essas opções
	[1] à vista dinheiro com 10% de desconto
	[2] à vista no cartão com 5% de desconto
	[3] em até 2x no cartão
	[4] 3x ou mais no cartão: 20% de juros
	''')
f = int(input('Qual a forma de pagamento? '))
vDinheiro = pNormal - (pNormal / 10)
vCartao = pNormal - (pNormal * 5) / 100
dCartao = pNormal / 2
if f == 1:
	print('Você pagará um valor de {:.2f}'.format(vDinheiro))
elif f == 2:
	print('Você pagará um valor de {:.2f}'.format(vCartao))
elif f == 3:
	print('Você pagará duas parcelas de {:.2f}'.format(dCartao))
elif f == 4:
	p = int(input('Em quantas parcelas? '))
	tCartao = pNormal + (pNormal * 20) / 100 
	divisao = tCartao/p
	print('Você pagará {} parcelas de {:.2f}'.format(p, divisao))
else:
	print('\033[31mValor inválido')