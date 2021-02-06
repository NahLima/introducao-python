#Exercício 1
#Escreva um programa que solicite o nome e o sobrenome do usuário.
#Ao final o programa deverá apresentar o nome completo do usuário na tela.

nome=input('Digite seu primeiro nome: ').strip().title() #strip tira o espaçamento e o title faz com que a cada palavra a primeira letra fique maiuscula
sobrenome=input('Digite seu sobrenome: ').strip().title()
print(f'{nome} {sobrenome}')
