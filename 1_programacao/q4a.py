#Ao fim de uma reuniao da area de Finanças Quantitativas, você decide colocar em
#pratica alguns conceitos novos que aprendeu. Para isso, programe a função
#montante_final que calcula o rendimento da taxa SELIC. A funcao deve ter os
#seguintes parametros, em ordem: capital, tempo (em anos) e taxa_selic, sendo esse
#ultimo um argumento padrao, ou seja, ele assume um valor padrão (4.25%) se não for
#assimilado durante a chamada da funcao. Dica: O calculo da taxa selic é feito da
#seguinte forma:    M = C*(1+i)**t

#inicializacao das variaveis em zero
C = 0
i = 0
t = 0

#criacao da funcao, suas operacoes e definicao dos paramentros (C, i, t)
def montante_final(C, i, t):
    C = float(input("Insira o valor capital: "))
    i = float(input("Insira o tempo em anos: "))
    t = float(input("Insira o valor da taxa: "))

    #Realizacao de operacao matematica para calcular a taxa SELIC
    M = C*(1+i)**t
    print("O valor do rendimento é ", M)

#chamada da funcao, que realiza as operacoes matematicas da linha 21 e solicitacoes de informacoes entre as linha 16 e 18
montante_final(C, i, t)
