# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#perguntas
v = float(input('Qual o valor da casa? '))
s = float(input('Qual o seu salário? '))
a = float(input('Em quantos anos você pretente pagar? '))

pMensal = v/(a * 12)
percenSalario = (s * 3)/10
print('Para pagar uma casa com parcelas de R$ {:.2f} ao mês em {} anos.'.format(pMensal, a))
if pMensal > percenSalario:
	print('O empréstimo foi NEGADO')
else:
	print('O empréstimo foi APROVADO.')
