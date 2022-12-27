# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
num = 0 #apresenta a variável ao python3
total = [] #apresenta a lista ao pyhton3
while num != 999:
	num = int(input('[Stop with 999] Type a number: '))
	total.append(num) #adiciona os números digitados à lista
	values_sum = sum(total) - 999 
print('{} valores foram digitados. A soma entre eles é {}.'.format(len(total) - 1, values_sum)) 