#Ao fim de uma reuniao na área de Processamento de Linguagem Natural do Turing USP,
#voce e seus amigos decidem construir o pior chatbot do mundo. Voces programam uma
#funcao que recebe uma frase de um usuario, e, caso essa frase seja uma pergunta,
#imprima a frase ”E eu vou saber? Sei la, procura no google”, caso nao seja ele
#responde “Ninguem liga”. Crie essa funcao onde o parametro e uma mensagem que
#pode ser uma pergunta ou nao. A função deve se chamar pior_chatbot, e deve
#receber como parametro a “frase” e imprimir a resposta.

mensagem = []
def pior_chatbot(mensagem):
    print("Olá. Posso ajudar em algo?")
    while True:
        #recebimento de mensagem/pergunta enviada
        mensagem = input()
        #chamamento da funcao resposta para processar mensagem/pergunta enviada
        resposta(mensagem)


def resposta(mensagem):
        #Se a mensagem lida possuir o caracter "?" na ultima posicao do vetor, entao ele retornara a mensagem da linha 22
        if [len(mensagem)-1] == "?":
            print("E eu vou saber? Sei la, procura no google.")
        ##Se a mensagem lida possuir o caracter "?" na ultima posicao do vetor, entao ele retornara a mensagem da linha 25
        elif [len(mensagem)-1] == "." or "!" or ":" or ";":                         
            print("Ninguem liga.")


pior_chatbot(mensagem)


