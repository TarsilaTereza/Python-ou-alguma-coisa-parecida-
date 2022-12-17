# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite um valor: '))
v3 = int(input('Digite um valor: '))
if v1 > v2 + v3 or v2 > v1 + v3 or v3 > v1 + v2:
	print('Isso não é um triângulo')
elif v1 == v2 == v3:
	print('Isso é um triângulo EQUILÁTERO')
elif v1 == v2 or v1 == v3 or v2 == v3:
	print('Isso é um triângulo ISÓSCELES')
else:
	print('Isso é um triângulo ESCALENO')
	

