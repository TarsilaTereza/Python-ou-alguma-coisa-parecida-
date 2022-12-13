# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math 
a = float(input('Digite o valor do ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('o seno é {:.2f}, o cosseno {:.2f} e a tangente é {:.2f}'.format(s, c, t))