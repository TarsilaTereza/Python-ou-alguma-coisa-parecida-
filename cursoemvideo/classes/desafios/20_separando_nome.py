# Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.n = input('Qual seu nome? ')
n = str(input('Qual eu nome? ')).strip()
nome = n.split()
print('O seu primeiro nome é {} e o seu último nome é {}'.format(nome[0], nome[len(nome)-1]))