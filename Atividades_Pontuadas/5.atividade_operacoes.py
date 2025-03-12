import os
os.system ("clear")
#Faça um programa que leia um código de operação (+,-,* ou /)
#e também dois valores inteiros A e B. 
#O programa deve calcular o resultado da operação escolhida aplicado
#a A e B. Por exemplo, se a operação escolhida foi
#* e A = 1 e B = 3, o programa deve fornecer como resultado o valor de 1*3, que é 3.

valor_um = int (input("Digite um valor: "))
valor_dois = int (input("Digite um valor: "))
operacao = str (input("Escolha a operação (+ | - | * | /): "))

match operacao:
    case "+":
        soma = valor_um + valor_dois
        print (f"A soma do {valor_um} + {valor_dois} é igual a: {soma}")
    case "-":
        sub = valor_um - valor_dois
        print (f"A subtração do {valor_um} - {valor_dois} é igual a: {sub}")
    case "*":
        multi = valor_um * valor_dois
        print (f"A multiplicação do {valor_um} X {valor_dois} é igual a: {multi}")
    case "/":
        div = valor_um / valor_dois
        print (f"A divisão do {valor_um} e {valor_dois} é igual a: {div}")


