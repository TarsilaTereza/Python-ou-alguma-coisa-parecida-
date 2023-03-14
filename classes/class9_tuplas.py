lanche = ('burguer', 'suco', 'pizza', 'pudim')
#Tuplas são imutáveis
# várias formas de for
# 1)
for cont in range(0, len(lanche)):
	print(f'vou comer {lanche[cont]}')
# 2)
for comida in lanche:
	print(f'vou comer {comida}')
print('comi muito')
# 3)
for posicao, comida in enumerate(lanche):
	print(f'vou comer {comida} na posição {posicao}')
# Posições e propriedades
print(lanche.index('pudim')) #pudim está na posição 3
