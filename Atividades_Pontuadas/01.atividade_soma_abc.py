import os
os.system ("clear")
#Faça um algoritmo que leia os valores A, B, C e imprima
#na tela se a soma de A + B é menor que C, caso contrário,
#imprima que a A + B é maior que C. 

valor_um = int (input("Digite um valor: "))
valor_dois = int (input("Digite um valor: "))
valor_tres = int (input("Digite um valor: "))

resultado =  valor_um + valor_dois

if resultado < valor_tres:
    print (f"{valor_um} + {valor_dois} é menor que {valor_tres}")
else:
    print (f"{valor_um} + {valor_dois} é maior que {valor_tres}")

print (f"O valor da soma é: {resultado}")
