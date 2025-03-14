import os
os.system ("clear")

print ("""
 Cor   |   Preço
Verde    R$ 10,00
Azul     R$ 20,00
Amarelo  R$ 30,00
Vermelho R$ 40,00""")
cd = str (input("Escolha o seu CD de acordo com a cor: "))

match cd:
    case "verde":
        print ("O valor desse disco é: R$ 10,00")
    case "azul":
        print ("O valor desse disco é: R$ 20,00")
    case "amarelo":
        print ("O valor desse disco é: R$ 30,00")
    case "vermelho":
        print ("O valor desse disco é: R$ 40,00")




