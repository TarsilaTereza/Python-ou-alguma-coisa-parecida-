
c = input('type something: ')
print('é um número?', c.isnumeric())
print('é uma palavra?',c.isalpha())
print('é um valor alfa numérico?',c.isalnum())

#refazendo...

a = int(input('type a number: '))
b = int(input('type other number: '))
s = a + b
print('the some worth {} and {} is {}.'.format(a, b, s))