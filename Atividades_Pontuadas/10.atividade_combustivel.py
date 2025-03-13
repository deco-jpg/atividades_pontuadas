import os
os.system ("clear")

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
