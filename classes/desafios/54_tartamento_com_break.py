# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
s = c = 0
while True:
	num = int(input('Type a number: '))
	if num == 999:
		break
	s += num
	c += 1
print(f'{c} numbers had been type, the sume between the values is {s}')