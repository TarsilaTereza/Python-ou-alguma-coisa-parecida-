#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite um número: '))
n3 = float(input('Digite um número: '))
lista = [n1, n2, n3] #adiciona os valores em uma lista
print(sorted(lista)) #coloca a lista em ordem crescente
print('O maior número é {}, e o menor é {}'.format(sorted(lista)[-1], sorted(lista)[0]))