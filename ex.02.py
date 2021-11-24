# 2. Escreva um algoritmo que leia dois números inteiros e exiba a multiplicação entre eles seo primeiro número for par; caso contrário, exiba a soma dos números.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um outro número: "))

re1 = num1 % 2

if re1 == 0:
    re2 = num1 * num2
    print ("Multiplicação: ",re2)

else:
    re3 = num1 + num2
    print("Soma: ",re3)







