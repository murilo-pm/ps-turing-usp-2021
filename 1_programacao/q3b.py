#Faca um programa que receba 4 notas, uma referente a cada bimestre de uma
#determinada materia de um aluno e que, ao final, diga se ele passou, está de
#recuperacao ou reprovou. 
#OBS: Assuma que o valor printado no output devera ter pelo menos duas casas decimais.

media = 0

primeiraNota = float(input("Por favor, insira a nota correspondente ao primeiro bimestre: "))
segundaNota = float(input("Por favor, insira a nota correspondente ao segundo bimestre: "))
terceiraNota = float(input("Por favor, insira a nota correspondente ao terceiro bimestre: "))
quartaNota = float(input("Por favor, insira a nota correspondente ao quarto bimestre: "))

media = (primeiraNota + segundaNota + terceiraNota + quartaNota)/4

if media < 3:
    print("Media:", media, ". Voce foi reprovado(a).")
elif media >= 3 and media < 6:
    print("Media:", media, ". Voce esta de recuperacao.")
elif media >= 6:
    print("Media:", media, ". Voce foi aprovado(a).")




