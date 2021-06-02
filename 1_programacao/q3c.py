#Durante uma reunião da área de Aprendizado por Reforço no Turing USP, você e seus
#amigos decidiram fazer uma competição em um jogo de corrida. Já que o vencedor
#ganhará um sorvetinho pago pelo grupo, você decide criar um programa que recebe a
#pontuação e o tempo de cada jogador e retorna quem foi o melhor. 
#vencedor -> maior pontuação por instante de tempo. 
#Considere o tempo em segundos.

#Pergunta inicial que vai determinar em qual condicional o programa sera iniciado
quantidadeJogadores = int(input("Quantos(a) jogadores(a) sao? "))

#Se houver somente um(a) jogador(a), ele(a) ganhara, pois nao eh necessaria a verificao
if quantidadeJogadores == 1:

    nome1 = input("Jogador(a) 1: ")
    pontuacao1 = float(input("Pontuacao 1: "))
    tempo1 = float(input("Tempo 1: "))
    print(nome1, "ganhou!")

#Se houver duas pessoas participando, verifica-se se o calculo da pontuacao da primeira pessoa eh maior que o da segunda, e vice-versa
elif quantidadeJogadores == 2:

    #insercao do nome
    nome1 = input("Jogador(a) 1: ")
    #insercao da pontuacao
    pontuacao1 = float(input("Pontuacao 1: "))
    #insercao do tempo
    tempo1 = float(input("Tempo 1: "))

    nome2 = input("Jogador(a) 2: ")
    pontuacao2 = float(input("Pontuacao 2: "))
    tempo2 = float(input("Tempo 2: "))

    #Calcula-se a pontuacao de cada uma das pessoas que estiverem participando do jogo
    calculoPontuacaoUm = pontuacao1/tempo1
    calculoPontuacaoDois = pontuacao2/tempo2

    #Caso a primeira pessoa tenha a maior pontuacao, ela sera declarada como vencedora
    if calculoPontuacaoUm > calculoPontuacaoDois:
        print(nome1, "ganhou!")
    #Caso contrario, o(a) outro(a) participante sera declarado vencedor(a)
    elif calculoPontuacaoDois > calculoPontuacaoUm:
        print(nome2, "ganhou!")

#A logica mencionada entre as linhas 20 e 36 se repetem, a unica diferencia eh a adicao de mais linha de codigos para a extracao de dados
#e determinacao do(a) vencedor(a) por meio de condicionais
elif quantidadeJogadores == 3:

    nome1 = input("Jogador(a) 1: ")
    pontuacao1 = float(input("Pontuacao 1: "))
    tempo1 = float(input("Tempo 1: "))

    nome2 = input("Jogador(a) 2: ")
    pontuacao2 = float(input("Pontuacao 2: "))
    tempo2 = float(input("Tempo 2: "))

    nome3 = input("Jogador(a) 3: ")
    pontuacao3 = float(input("Pontuacao 3: "))
    tempo3 = float(input("Tempo 3: "))

    calculoPontuacaoUm = pontuacao1/tempo1
    calculoPontuacaoDois = pontuacao2/tempo2
    calculoPontuacaoTres = pontuacao3/tempo3

    if calculoPontuacaoUm > calculoPontuacaoDois and calculoPontuacaoUm > calculoPontuacaoTres:
        print(nome1, "ganhou!")
    elif calculoPontuacaoDois > calculoPontuacaoUm and calculoPontuacaoDois > calculoPontuacaoTres:
        print(nome2, "ganhou!")
    elif calculoPontuacaoTres > calculoPontuacaoUm and calculoPontuacaoTres > calculoPontuacaoDois:
        print(nome3, "ganhou!")

elif quantidadeJogadores == 4:

    nome1 = input("Jogador(a) 1: ")
    pontuacao1 = float(input("Pontuacao 1: "))
    tempo1 = float(input("Tempo 1: "))

    nome2 = input("Jogador(a) 2: ")
    pontuacao2 = float(input("Pontuacao 2: "))
    tempo2 = float(input("Tempo 2: "))

    nome3 = input("Jogador(a) 3: ")
    pontuacao3 = float(input("Pontuacao 3: "))
    tempo3 = float(input("Tempo 3: "))

    nome4 = input("Jogador(a) 4: ")
    pontuacao4 = float(input("Pontuacao 4: "))
    tempo4 = float(input("Tempo 4: "))

    calculoPontuacaoUm = pontuacao1/tempo1
    calculoPontuacaoDois = pontuacao2/tempo2
    calculoPontuacaoTres = pontuacao3/tempo3
    calculoPontuacaoQuatro = pontuacao4/tempo4

    if calculoPontuacaoUm > calculoPontuacaoDois and calculoPontuacaoUm > calculoPontuacaoTres and calculoPontuacaoUm > calculoPontuacaoQuatro:
        print(nome1, "ganhou!")
    elif calculoPontuacaoDois > calculoPontuacaoUm and calculoPontuacaoDois > calculoPontuacaoTres and calculoPontuacaoDois > calculoPontuacaoQuatro:
        print(nome2, "ganhou!")
    elif calculoPontuacaoTres > calculoPontuacaoUm and calculoPontuacaoTres > calculoPontuacaoDois and calculoPontuacaoTres > calculoPontuacaoQuatro:
        print(nome3, "ganhou!")
    elif calculoPontuacaoQuatro > calculoPontuacaoUm and calculoPontuacaoQuatro > calculoPontuacaoDois and calculoPontuacaoQuatro > calculoPontuacaoTres:
        print(nome4, "ganhou!")
