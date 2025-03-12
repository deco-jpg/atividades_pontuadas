import os
os.system ("cls")

print (""""
  ATÉ 5KG          | ACIMA DE 5KG   
Maçã: 1,80R$ KG      Maçã: 1,50R$ KG

Morango: 2,50R$ KG   Morango: 2,20R$ KG""")

fruta = str (input("Escolha entre Maçã ou Morango: ")) .lower ()

match fruta:
    case "maçã":
        quantidade = int (input("Escolha a quantidade desejada (em KG): "))
        valor1 = quantidade * 1.80
        valor2 = quantidade * 1.50
        if quantidade >= 10 or valor2 > 15:
            print (f"A quantidade de {quantidade}KG das maçãs custará: {valor2}")
        elif quantidade <5:
            print (f"A quantidade de {quantidade}KG das maçãs custará: {valor1}")
        elif quantidade <5:
            valor1 = quantidade * 1.50
            print (f"A quantidade de {quantidade}KG das maçãs custara: {valor1}")
    case "morango":
        quantidade = int (input("Escolha a quantidade desejada: "))
        valor1 = quantidade * 1.80
        valor2 = quantidade * 1.50
        if quantidade >= 10 or valor2 > 15:
            print (f"A quantidade de {quantidade}KG dos morangos custará: {valor2}")
        elif quantidade <5:
            print (f"A quantidade de {quantidade}KG dos morangos custará: {valor1}")
        elif quantidade <5:
            valor1 = quantidade * 1.50
            print (f"A quantidade de {quantidade}KG dos morangos custara: {valor1}")

