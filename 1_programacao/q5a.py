#Crie uma funcao, chamada “cifra”, que recebe como entrada uma mensagem (string) e
#um numero, referente a chave da codificacao da cifra de Caesar, e retorna a
#mensagem cifrada.

alfabeto = "abcdefghijklmnopqrstuvxwyz"
mensagem = ""
chave = 0
shift = 3

def cifra(mensagem, chave):
    mensagem = input("Por favor, insira uma mensagem: ")
    chave = int(input("Por favor, insira uma chave: "))
    #para cada caracter da mensagem, descobre-se o indice correspondente no alfabeto
    for c in mensagem:
        #mensagemVazio = espaco vazio entre palavras
        mensagemVazio = ""              
        c_index = alfabeto.index(c)
        #busca do alfabeto no indice + shift, ou seja, o caracter + 3, que representa o avanco em tres "casas"
        #a funcao de modulo (%) entra para dividir o numero pelo tamanho (len) do alfabeto
        #por exemplo, se o resto daquilo que foi dividido por zero, entao o equivalente a esse caracter torna-se
        #a letra "a"
        mensagem += alfabeto[(c_index + shift) % len(alfabeto)]
        #se houver um espaco vazio, ele eh adicionado a string sem sofrer alteracoes
        return mensagem

cifra(mensagem, chave)
