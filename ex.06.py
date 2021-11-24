# 6. Escreva um algoritmo que receba o primeiro termo e a razão de uma PG. No final mostre os 5 primeiros termos dessa progressão.

a1 = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão: "))

cont = 1 
while cont <=5:
    razao = razao * a1
    cont = cont + 1

    print (razao)