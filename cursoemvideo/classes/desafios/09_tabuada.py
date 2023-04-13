#tabuada
n = int(input('digite um número'))
t=1
while (t <= 10):
    continha = n*t
    print('{} x {} é igual a {}'.format(n, t, continha))
    t+=1