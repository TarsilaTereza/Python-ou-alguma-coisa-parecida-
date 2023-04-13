	# Crie um programa que leia o nome completo de uma pessoa e mostre:
n = input('Qual seu nome? ')
# – O nome com todas as letras maiúsculas e minúsculas.
print('Seu nome maiúsculo é {} e minúsculo é {}'.format(n.upper(), n.lower()))
# – Quantas letras ao todo (sem considerar espaços).
print('Possui {} letras'.format(len(n)))
# – Quantas letras tem o primeiro nome.
quebrado = n.split()
print('O primeiro nome possui {} letras'.format(len(quebrado[0])))
