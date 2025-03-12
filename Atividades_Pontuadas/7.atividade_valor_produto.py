import os
os.system ("clear")

print("""
Produtos:
Arroz | Feijão

Código | Valor
1 \t   3   
2 \t   5
""")

produto = int(input("Digite o que você deseja: """))

match produto:
    case 1:
        preco = 3
        quantidade = int (input("Quantidade: "))
        valor = preco * quantidade
        if quantidade <= 5:
            desconto = valor - (valor * 0.2)
        elif quantidade <=10:
            desconto = valor - (valor * 0.3)
        elif quantidade > 10:
            desconto = valor - (valor * 0.5)
            


    case 2:
        preco = 5
        quantidade = int (input("Quantidade: "))
        valor = preco * quantidade
        if quantidade <= 5:
            desconto = valor - (valor * 0.2)
        elif quantidade <=10:
            desconto = valor - (valor * 0.3)
        elif quantidade > 10:
            desconto = valor - (valor * 0.5)
    case _:
        print ("Opção Inválida")

print (f"\nPreço do produto: {preco}")
print (f"Quantidade desejada: {quantidade}")
print (f"Valor total: {valor}")
print (f"Valor com desconto: {desconto}")



        
        




    


        

    
