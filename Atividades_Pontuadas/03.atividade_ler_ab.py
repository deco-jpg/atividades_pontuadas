import os
os.system ("clear")

#Faça um algoritmo que leia dois valores inteiros A e B
#se os valores forem iguais deverá se somar os dois,
#caso contrário multiplique A por B. Ao final de qualquer
#um dos cálculos deve-se atribuir o resultado para
#uma variável C e mostrar seu conteúdo na tela.

valor_um = int (input("Digite um valor: "))
valor_dois = int (input("Digite um valor: "))

if valor_um == valor_dois:
    soma = valor_um + valor_dois
    print ("\nValores iguais! ")
    print (f"O resultado da soma é: {soma}")
else:
    multi = valor_um * valor_dois
    print ("Os valores não são iguais! ")
    print (f"O resultado da multiplicação é: {multi}")
