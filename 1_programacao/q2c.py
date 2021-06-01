#Pensando em marcar uma reuniao com outros membros do Turing USP, você precisa
#decidir qual vai ser o melhor dia da semana para isso. Representando cada dia da
#semana por um numero, (Domingo: 0, Segunda-feira: 1, até Sabado: 6), faça um
#programa que seja capaz de receber votos para cada dia da semana e, caso o numero
#inserido seja -1, devolva o numero de votos que cada dia da semana recebeu e qual foi
#o dia com maior numero de votos.

#Inicializacao das variaveis em zero
contador = 0
maiorNumero = 0
menorNumero = 0
somaDomingo = somaSegunda = somaTerca = somaQuarta = somaQuinta = somaSexta = somaSabado = 0

#repetidor para insercao dos 6 votos    (Domingo: 0, Segunda-feira: 1, até Sábado: 6)
#6 entradas = 6 votos
while contador != -1:
    #int(input(mensagem)) --> transforma o valor da entrada em inteiro
    numero = int(input("Por favor, vote [0] domingo, [1]segunda, [2]terca, [3]quarta, [4]quinta, [5]sexta e [6]sabado: "))
    
    #a cada nova rodada soma-se 1 ao contador
    contador += 1
    #somatoria de todos os votos que serão inseridos pelos(as) usuarios(as), de acordo com o dia da semana
    if numero == 0:
        somaDomingo += (numero + 1)/1   #Soma-se o numero do voto a ele mesmo para ajustar a exibicao dos votos
        #contador += 1
    elif numero == 1:
        somaSegunda += numero / 1   #Divide-se o numero do voto por ele mesmo para ajustar a exibicao dos votos
        #contador += 1
    elif numero == 2:
        somaTerca += numero / 2     #Divide-se o numero do voto por ele mesmo para ajustar a exibicao dos votos
        #contador += 1
    elif numero == 3:
        somaQuarta += numero / 3    #Divide-se o numero do voto por ele mesmo para ajustar a exibicao dos votos
        #contador += 1
    elif numero == 4:
        somaQuinta += numero / 4    #Divide-se o numero do voto por ele mesmo para ajustar a exibicao dos votos
        #contador += 1
    elif numero == 5:
        somaSexta += numero / 5     #Divide-se o numero do voto por ele mesmo para ajustar a exibicao dos votos
        #contador += 1
    elif numero == 6:
        somaSabado += numero / 6    #Divide-se o numero do voto por ele mesmo para ajustar a exibicao dos votos
        #contador += 1
    #Quando o(a) usuario digita "-1" o programa vai parar e vai retornar os resultados da votacao
    if numero == -1:
        #Os resultados sao apresentados com uma casa decimal, pois fora realizada uma divisao para a correcao de um bug na exibicao dos votos
        print("Resultados:")
        print("Domingo =", somaDomingo)
        print("Segunda =", somaSegunda)
        print("Terca =", somaTerca)
        print("Quarta =", somaQuarta)
        print("Quinta =", somaQuinta)
        print("Sexta =", somaSexta)
        print("Sabado =", somaSabado)

        #condicionais para estabelecer o dia vencedor a cada nova rodade de votacao
        if somaDomingo > somaSegunda and somaTerca and somaQuarta and somaQuinta and somaSexta and somaSabado:
            print("O dia vencedor e Domingo")

        if somaSegunda > somaDomingo and somaTerca and somaQuarta and somaQuinta and somaSexta and somaSabado:
            print("O dia vencedor e Segunda")

        if somaTerca > somaDomingo and somaSegunda and somaQuarta and somaQuinta and somaSexta and somaSabado:
            print("O dia vencedor e Terca")

        if somaQuarta > somaDomingo and somaSegunda and somaTerca and somaQuinta and somaSexta and somaSabado:
            print("O dia vencedor e Quarta")

        if somaQuinta > somaDomingo and somaSegunda and somaTerca and somaQuarta and somaSexta and somaSabado:
            print("O dia vencedor e Quinta")
        
        if somaSexta > somaDomingo and somaSegunda and somaTerca and somaQuarta and somaQuinta and somaSabado:
            print("O dia vencedor e Sexta")

        if somaSabado > somaDomingo and somaSegunda and somaTerca and somaQuarta and somaQuinta and somaSexta:
            print("O dia vencedor e Sabado")
        

        
        
    
    
