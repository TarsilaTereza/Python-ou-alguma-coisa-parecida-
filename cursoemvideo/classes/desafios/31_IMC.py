# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso

# – Entre 18,5 e 25: Peso Ideal

# – 25 até 30: Sobrepeso

# – 30 até 40: Obesidade

# – Acima de 40: Obesidade Mórbida
#peso dividido pela altura ao quadrado
h = float(input('Qual sua altura em centímetros? '))
p = float(input('Qual seu peso em kilogramas? '))
hmetros = h / 100 #transforma a altura de centímetros para metros
imc = p / hmetros**2
if imc < 18.5:
	print('Seu IMC é {:.1f} você está ABAIXO do peso.'.format(imc))
elif imc < 25:
	print('Seu IMC é {:.1f}, você está no peso IDEAL.'.format(imc))
elif imc < 30:
	print('Seu IMC é {:.1f}, você está ACIMA do peso.'.format(imc))
elif imc < 40:
	print('Seu IMC é {:.1f}, você está OBESO.'.format(imc))
else:
	print('Seu IMC é {:.1f}, você está em grau de OBESIDADE MÓRBIDA.'.format(imc))