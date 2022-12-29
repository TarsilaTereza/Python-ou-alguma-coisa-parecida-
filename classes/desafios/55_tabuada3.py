# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
c = 1
while c <= 10:
	num = int(input('Que tabuada você precisa?: '))
	if num < 0:
		break
	for c in range (1, 11):
		print(f'{c} X {num} = {c * num}')
print('Obrigada por usar este programa')