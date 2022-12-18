# Faça um programa que calcule a soma de todos os números ímpares entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0 #acumulador
cont = 0 #contador, quantos termos foram acumulados
for c in range(1, 501, 2):  #começando do 1 pulando de dois em dois vai de ímpar em ímpar
	if c % 3 == 0: #apenas os números que forem divisíveis por 3
		soma += c # soma = soma + c
		cont += 1
print('a soma dos {} valores formatados é {}'.format(cont, soma))