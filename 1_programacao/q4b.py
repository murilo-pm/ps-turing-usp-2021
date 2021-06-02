#Ao fim de uma reuniao na área de Processamento de Linguagem Natural do Turing USP,
#voce e seus amigos decidem construir o pior chatbot do mundo. Voces programam uma
#funcao que recebe uma frase de um usuario, e, caso essa frase seja uma pergunta,
#imprima a frase ”E eu vou saber? Sei la, procura no google”, caso nao seja ele
#responde “Ninguem liga”. Crie essa funcao onde o parametro e uma mensagem que
#pode ser uma pergunta ou nao. A função deve se chamar pior_chatbot, e deve
#receber como parametro a “frase” e imprimir a resposta.


def iniciar():
    print("Olá. Posso ajudar em algo?")
    while True:
        #recebimento de mensagem/pergunta enviada
        mensagem = input()
        #processar mensagem/pergunta enviada
        processamentoMensagem(mensagem)

def processamentoMensagem(mensagem):
    if mensagem == ["?"]:
        print("E eu vou saber? Sei la, procura no google.")
    elif mensagem == [(".", "!", ":", ";")]:
        print("Ninguem liga.")


iniciar()

