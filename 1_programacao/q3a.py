#Faca um Programa que receba altura e peso e imprima o IMC e a condicao da pessoa
#segundo a tabela abaixo. DICA: IMC = peso / altura², sendo o peso em kg e a altura
#em metros. 
#OBS 1: Imprima o IMC com pelo menos 2 casas decimais. 
#OBS 2: Assuma que o valor printado no output deverá ter pelo menos duas casas decimais.

imc = 0

altura = float(input("Por favor, agora, informe a sua altura em metros: "))
peso = int(input("Por favor, informe o seu peso: "))


imc = peso/(altura*altura)

if imc < 16:
    print("IMC =", imc, "; Condicao Subpeso Severo")

elif imc >= 16 and imc < 20:
    print("IMC =", imc, "; Condicao Subpeso")

elif imc >= 20 and imc < 25:
    print("IMC =", imc, "; Condicao Normal")

elif imc >= 25 and imc < 30:
    print("IMC =", imc, "; Condicao Sobrepeso")

elif imc >= 30 and imc < 40:
    print("IMC =", imc, "; Condicao Obeso")

elif imc >= 40:
    print("IMC =", imc, "; Condicao Obeso Mórbido")
