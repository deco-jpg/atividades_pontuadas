import os
os.system ("clear")
#Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte
#forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que
#O preço do litro da gasolina é R$ 6,59 e o preço do litro do álcool é R$ 3,79.

litros = float (input("Escola a quantidade de litros: "))
tipo_combustivel = input ("Escolha o tipo de combustivel (A- Alcool | (G- Gasolina: ") .strip() .upper()
gasolina = 6.59
alcool = 3.79

match tipo_combustivel:
    case "A":
        preço_por_litro = alcool
        desconto = 0.2 if litros <= 25 else 0.4
    case "G":
        preço_por_litro = gasolina
        desconto = 0.3 if litros <= 25 else 0.5
    case _:
        print ("Opção Inválida! ")

#Calculos

valor_total = preço_por_litro * litros
valor_desconto = valor_total * desconto
valor_pago = valor_total - valor_desconto

print (f"O valor a ser pago será: {valor_pago}")
