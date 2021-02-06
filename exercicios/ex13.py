#Considere a tupla1 e responda as seguintes questões:



tupla1=('A','B','A','Z','Z','X','A','E','K','G','H')



#a) mostre na tela o tamanho desta tupla;
print(f'Tamanho da tupla1:',len(tupla1))

#b) ordene a tupla e mostre o resultado na tela;
print(sorted(tupla1))

#c) mostre na tela o número de ocorrências da string 'A';
print("Número de ocorrências de 'A' ",tupla1.count('A'))

#d) mostre na tela o número de ocorrências da string 'B';
print("Número de ocorrências de 'B' ",tupla1.count('B'))

#e) mostre na tela o índice da string 'X';
print("Índice da string 'X' ",tupla1.index('X'))

#f) mostre na tela o último elemento da tupla1.
print(tupla1[-1])

