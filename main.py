# Faça um programa que receba do usuário um número inteiro e imprima na tela a tabuada 
# desse número (em colunas).


num=int(input('Digite um número inteiro:'))

cont = 1

print('Tabuada no número %d' %(num))

while cont<=10:
    resultado = num * cont
    print('%d vezes %d = %d\n' %(num,cont,resultado))
    cont = cont + 1
>>>>>>> 0aa89126600ad4d039c5630c718cdbe637dbe075