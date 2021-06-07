
mensagem = []

def pior_chatbot(mensagem):
    print("Olá. Posso ajudar em algo?")
    while True:
        #recebimento de mensagem/pergunta enviada
        mensagem = input()
        if [len(mensagem)-1] == "?":
            print("E eu vou saber? Sei la, procura no google.")
        elif [len(mensagem)-1] == ".":                       # or "!" or ":" or ";"  
            print("Ninguem liga.")

pior_chatbot(mensagem)