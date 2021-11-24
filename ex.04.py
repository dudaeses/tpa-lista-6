# 4. Escreva um algoritmo para imprimir na tela a tabuada de um número informado pelo usuário.

num = int(input("Digite um número: "))

for i in range (0,11):
    produto = num * i

    print(f"{num} x {i} = {produto}")