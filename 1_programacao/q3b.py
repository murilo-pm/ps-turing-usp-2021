#Faca um programa que receba 4 notas, uma referente a cada bimestre de uma
#determinada materia de um aluno e que, ao final, diga se ele passou, está de
#recuperacao ou reprovou. 
#OBS: Assuma que o valor printado no output devera ter pelo menos duas casas decimais.

#inicializacao da variavel em zero
media = 0

#insercoes de notas de acordo com o bimestre
primeiraNota = float(input("Por favor, insira a nota correspondente ao primeiro bimestre: "))
segundaNota = float(input("Por favor, insira a nota correspondente ao segundo bimestre: "))
terceiraNota = float(input("Por favor, insira a nota correspondente ao terceiro bimestre: "))
quartaNota = float(input("Por favor, insira a nota correspondente ao quarto bimestre: "))

#formula responsavel por realizar o calculo da media de cada estudante
media = (primeiraNota + segundaNota + terceiraNota + quartaNota)/4

#sequencia de condicionais responsaveis por enquadrar o(a) aluno(a) em determinada situacao a depender da sua media 
if media < 3:
    print("Media:", media, ". Voce foi reprovado(a).")
elif media >= 3 and media < 6:
    print("Media:", media, ". Voce esta de recuperacao.")
elif media >= 6:
    print("Media:", media, ". Voce foi aprovado(a).")




