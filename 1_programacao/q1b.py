#Seu programa deve receber dois nomes e duas idades, por meio de 4 inputs, depois
#voce deve atribuir o valor da variavel da idade 1 para a idade 2, invertendo-as.
#OBS: Os valores devem ser realmente trocados, nao apenas printados um no lugar do
#outro. Ou seja, ao final, quando a pessoa printar idade2 na tela, o valor que aparece
#tem que ser o original da idade1.

#solitacao do nome
nome1 =  input("Qual e o nome? ")
#solitacao da idade1
idade1 = input("Qual e a idade? ")
#solitacao do nome
nome2 = input("Qual e o nome? ")
#solitacao da idade2
idade2 = input("Qual e a idade? ")

#idade1 vira idade2 e idade2 vira idade1. Assim sendo: idade1 recebe idade2, e vice-versa
idade1, idade2 = idade2, idade1

#exibicao e concatenacao
print("A idade de", nome1, "e", idade1, "anos. A idade de", nome2, "e", idade2, "anos.")