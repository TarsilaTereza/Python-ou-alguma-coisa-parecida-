#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = int(input("Quantos quilômetros o carro percorreu?"))
d = int(input("Por quantos dias ele foi alugado?"))
p = (60*d)+(0.15*km)
print("O aluguel do carro custará {} reais.".format(p))