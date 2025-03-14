import os
os.system ("cls")

valor_emprestimo = float (input("Digite o valor do emprestimo: ")) 
renda_mensal = float (input("Digite o valor da sua renda mensal: "))
valor_prestacao = int (input("Escolha a quantidade de prestações: "))

prestacao = valor_emprestimo / valor_prestacao
emprestimo = renda_mensal * 10
desconto_prestacao = renda_mensal * 0.03

if valor_emprestimo <= valor_prestacao and valor_prestacao <= renda_mensal:
    print ("Emprestimo concedido! ")
else:
    print ("Emprestimo negado! ")
