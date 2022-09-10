#tratamento de dados
# fatiamento de string
frase = ('Curso em vídeo Python')
print(len(frase)) #quantidade de caracteres
print(frase.find('vídeo')) #encontra em qual posição começa 'vídeo'
print(frase.count('o', 0, 22)) #conta do 0 ao 21 quantos 'o's têm 
print(frase[15:]) #após o carac. 15, que palavras tem
print('Curso' in frase)
print(frase.replace('Python', 'Android')) #troca
print(frase.upper())
a = input('Insira frase')
print(a.strip())#eliminar espaços inicial e final vazio (lstrip e rstrip)
print(a.split())#quebra a lista de acordo com os espaços em listas - entre os pelotões cobrir
'-'.join(a)