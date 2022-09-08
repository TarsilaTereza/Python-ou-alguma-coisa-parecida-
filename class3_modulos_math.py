#import bebida (tudo)
#é diferente de:
#from bebida import suco (só suco, economiza memória) 
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num,raiz))
# arrendondar para cima math.ceil(raiz), para baixo floor
# {:.2f} é para printar somente duas casas decimais após a vírgula

#SE QUISESSE USAR O from PARA IMPORTAR APENAS O sqrt

from math import sqrt
num = int(input('Type a number: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, int(math.floor(raiz)))) #o resultado da raiz é o inteiro mais próximo (arredondado para baixo)