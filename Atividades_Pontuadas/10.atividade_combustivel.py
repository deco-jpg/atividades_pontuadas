import os
os.system ("clear")
#Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte
#forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que
#O preço do litro da gasolina é R$ 6,59 e o preço do litro do álcool é R$ 3,79.

import os
os.system ("cls")

print (""""
       
 Álcool:                     |   Gasolina
 Até 25L:                        Até 25L:                     
 Desconto de 2% p/ Litro.        Desconto de 3% p/ Litro.

 Acima de 25L:                   Acima de 25L:
 Desconto de 4% p/ Litro.        Desconto de 5% p/ Litro.
""")
tipo_combustivel = input ("Escolha o tipo de combustivel (A- Alcool | (G- Gasolina: ") .strip() .upper()
litros = float (input("Escola a quantidade de litros: "))
alcool = 3.79
gasolina = 6.59
litro_alcool = litros * 3.79
litro_gasolina = litros * 6.59

match tipo_combustivel:
    case "A":
        if litros <= 25:
            calculo_desc = litro_alcool * 0.02
            total_pagar = litro_alcool - calculo_desc
            print (f"O valor a ser pago é: {total_pagar:.2f}")
        else:
            calculo_desc = litro_alcool * 0.04
            total_pagar = litro_alcool - calculo_desc
            print (f"O valor a ser pago é: {total_pagar:.2f} ")
    case "G":
        if litros <= 25:
            calculo_desc = litro_gasolina * 0.03
            total_pagar = litro_alcool - calculo_desc
            print (f"O valor a ser pago é: {total_pagar:.2f}")
        else:
            calculo_desc = litro_gasolina * 0.05
            total_pagar = litro_alcool - calculo_desc
            print (f"O valor a ser pago é: {total_pagar:.2f}")
    case _:
        print ("Opção Inválida!")

            
