# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import sqrt
o = float(input('Digite o valor do cateto oposto: '))
a = float(input('Digite o valor do cateto adjacente: '))
h = o**2 + a**2
print('o valor da hipotenusa é {}'.format(sqrt(h)))

# possibilidadess

# import math
# o = float(input('Digite o valor do cateto oposto: '))
# a = float(input('Digite o valor do cateto adjacente: '))
# h = math.hypot(o, a)
# print('o valor da hipotenusa é {}'.format(h))

from math import hypot
o = float(input('Digite o valor do cateto oposto: '))
a = float(input('Digite o valor do cateto adjacente: '))
h = hypot(o, a)
print('o valor da hipotenusa é {}'.format(h))