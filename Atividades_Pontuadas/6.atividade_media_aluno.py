import os
os.system ("clear")

nome = str (input("Digite seu nome: "))
nota_um = int (input("Digite a primeira nota: "))
nota_dois = int (input("Digite a segunda nota: "))

soma = nota_um + nota_dois
media = soma / 2

print (f"Nome: {nome}")
print (f"A média do aluno é: {media}")

if media >= 6:
    print ("Aprovado! ")
elif media == 4:
    print ("Recuperação! ")
else:
    print ("Reprovado! ")