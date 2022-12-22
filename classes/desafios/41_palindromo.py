# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = input('Digite uma frase: ').upper().strip().replace(' ', '') #replace substitui espaço por nada
if frase == frase[::-1]:
	print('essa frase é um palíndromo')
else:
	print('essa frase não é um palíndromo')