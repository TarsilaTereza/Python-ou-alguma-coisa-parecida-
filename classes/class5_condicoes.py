# nome = str(input('Qual seu nome? '))
# if nome == 'tarsila':
# 	print('Que nome lindo')
# else:
# 	print('Seu nome é tão mixuruca')
# print('Boa tarde, {}'.format(nome))

# passou ou não passou de ano?
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
media = (n1 + n2)/2
if media < 6:
	print('Sua média foi {}, você está de recuperação'.format(media))
else:
	print('Sua média foi {}, você está aprovado!'.format(media))