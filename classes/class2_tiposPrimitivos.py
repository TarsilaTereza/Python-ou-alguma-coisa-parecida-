# int - 12; 13; 9082; -9887876
# float - 3.4; 9.8; 7.0
# bool - True; False
# string - "olá"; "aoba"; ""

n1 = input('digite o valor')
print(type(n1)) #vai retornar uma string. tipo primitivo não especificado.

n2 = int(input('type a value'))
print(type(n2)) #retornou int.

n3 = int(input('type other value'))

s = n2 + n3
print('the sum between', n2, "and", n3, 'is', s)

#utilizando o .format()
print('the sum between {} and {} is {}'.format(n2, n3, s))
