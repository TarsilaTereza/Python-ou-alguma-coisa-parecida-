# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
n = int(input('Digite um número: '))
o = print('''\033[0;35mEscolha uma base de conversão:\033[m
	[1] Binário
	[2] Octal
	[3] Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
	print('O número {} convertido para binário é {}'. format(n, bin(n)[2:]))
elif opcao == 2:
	print('O número {} convertido para octal é {}'. format(n, oct(n)[2:]))
elif opcao == 3:
	print('O número {} convertido para hexadecimal é {}'. format(n, hex(n)[2:]))
else:
	print('Escolha uma opção válida')
