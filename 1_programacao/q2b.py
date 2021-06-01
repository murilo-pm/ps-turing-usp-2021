#Agora, seu programa deve pegar os números da lista, como no exercício anterior, e
#calcular a média e a moda dela. Se a lista for amodal, o programa deve printar isso. A
#média deve ser impressa com pelo menos duas casas decimais.

#OBS: Não é permitida a importação de bibliotecas
#OBS2: Assuma que o valor printado no output deverá ter pelo menos duas casas decimais.

contador = 0
maiorNumero = 0
menorNumero = 0
soma = 0
media = 0
moda = 0 #numero que mais aparece na sequencia de dados

#repetidor para insercao dos 6 numeros
#while contador < 6:

#int(input(mensagem)) --> transforma o valor da entrada em inteiro
numero1 = int(input("Por favor, digite um numero: "))
numero2 = int(input("Por favor, digite um numero: "))
numero3 = int(input("Por favor, digite um numero: "))
numero4 = int(input("Por favor, digite um numero: "))
numero5 = int(input("Por favor, digite um numero: "))
numero6 = int(input("Por favor, digite um numero: "))
#somatoria de todos os numeros que serão inseridos pelo(a) usuario(a)
soma = numero1 + numero2 + numero3 + numero4 + numero5 + numero6
#a cada nova rodada soma-se 1 ao contador
contador += 1
#calculo da media
media = soma/6

#Aqui, tem-se uma sequencia de condicionais para a verificacao da moda, comparando dois valores já inseridos
if numero1 == numero2:
    print("A media e", media, ". A moda e", numero1)
elif numero2 == numero3:
    print("A media e", media, ". A moda e", numero2)
elif numero3 == numero4:
    print("A media e", media, ". A moda e", numero3)
elif numero4 == numero5:
    print("A media e", media, ". A moda e", numero4)
elif numero5 == numero6:
    print("A media e", media, ". A moda e", numero5)
#A partir daqui inicia-se uma verificacao de modas por meio da insercao de numeros nao sequencial,
#tentando abranger o maior numero de cenarios possiveis
elif numero1 == numero3:
    print("A media e", media, ". A moda e", numero1)
elif numero2 == numero4:
    print("A media e", media, ". A moda e", numero2)
elif numero3 == numero6:
    print("A media e", media, ". A moda e", numero3)
elif numero4 == numero6:
    print("A media e", media, ". A moda e", numero4)
elif numero5 == numero1:
    print("A media e", media, ". A moda e", numero5)
elif numero6 == numero1:
    print("A media e", media, ". A moda e", numero6)
elif numero2 == numero6:
    print("A media e", media, ". A moda e", numero6)
else:
 print("A media e", media, ". A lista e amodal.")

#NOTA: tentar realizar a verificacao da moda utilizando verificacao com vetores