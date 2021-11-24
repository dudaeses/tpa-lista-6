# 7. Escreva  um  algoritmo que  receba uma  média  (de  zero  a  10)  e  uma  frequência  (de  zero  a 100) de um(a) aluno(a) e:
# a) Se  o  aluno  possuir  frequência  menor  que  75%,  exiba  a  mensagem:  “Você  foi reprovado”; 
# b) Se o aluno possuir frequência maior que 75% e média menor que 7, exiba a mensagem “Você está de recuperação”;
# c) Se  o  aluno  possuir  frequência  maior  que  75%  e  médiamaior  ou  igual  que  7,  exiba  a mensagem “Você foi aprovado”.

media = int(input("Média do(a) aluno(a) [0/10]: "))
freq = int(input("Frequência do(a) aluno(a) [0/100%]: "))

if freq < 75:
    print ("Você foi reprovado(a).")

if freq > 75 and media < 7:
    print ("Você está de recuperação.")

if freq > 75 and media >= 7:
    print ("Você foi aprovado(a).")


