# laço de repertição
	# - variável de controle
for c in range(0, 6):
	print(c, 'hello world')
print('FIM')

print('-=-' * 10)

for a in range(6, 0, -1):
	print(a)

print('-=-' * 10)

for a in range(0, 6, 2):
	print(a)

print('-=-' * 10)
s = 0
for d in range(0, 4):
	n = int(input('Digite um número: '))
	s += n
print('O somatório dos números selecionados é', s)