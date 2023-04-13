# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sex = str(input('Insira seu gênero: ')).strip().upper()[0]
while sex not in 'MmFf':
	sex = str(input('Dado inválido. Insira seu gênero: ')).strip().upper()[0]
print(sex)