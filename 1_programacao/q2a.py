#Seu programa deve receber 6 números e armazená-los numa lista. A entrada dos
#números será feita um de cada vez. Em seguida, ele deve printar a soma de todos os
#elementos dessa lista, o maior número e o menor. 
#OBS: Funções prontas, como min(), max() e sum() não serão aceitas. 

#Inserções de numero aleatorios, de acordo com a vontade do(a) usuário(a)
#Inicializacao das variaveis em zero
contador = 0
maiorNumero = 0
menorNumero = 0
soma = 0

#repetidor para insercao dos 6 numeros
while contador < 6:
    #int(input(mensagem)) --> transforma o valor da entrada em inteiro
    numero = int(input("Por favor, digite um numero: "))
    #somatoria de todos os numeros que serão inseridos pelo(a) usuario(a)
    soma += numero
    #a cada nova rodada soma-se 1 ao contador
    contador += 1
    #se o contador for 1, entao as variaveis maiorNumero e menorNumero passarao a ser o numero que acaba de ser inserido pelo(a) usuario(a)
    if contador == 1:
        maiorNumero = menorNumero = numero
    #Caso contrario    
    else:
        #Se o numero recem inserido for maior que o valor definido na linha 22, entao o maior numero passa a ser o ultimo numero inserido  
        if numero > maiorNumero:
            #Aqui: o maiorNumero muda conforme o valor que acaba de entrar, o maiorNumero recebe o valor da variavel numero
            maiorNumero = numero
        #Se o numero recem inserido for menor que o valor definido na linha 22, entao o menor numero passa a ser o ultimo numero inserido  
        if numero < menorNumero:
            #Aqui: o menorNumero muda conforme o valor que acaba de entrar, o menorNumero recebe o valor da variavel numero
            menorNumero = numero
print("A soma dos elementos da lista e", soma, ", o maior numero e", maiorNumero, "e o menor e", menorNumero)