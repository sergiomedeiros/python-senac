"""
Exibindo Curso Python e Django - Aula 2.pdf…
Desafios
2 – Desenvolva um programa que sorteie um nome
aleatoriamente dentro de uma lista contendo vários nomes;
"""

import random
nome=["sergio","anne","bel","pedro","andre"]

i = 0
while i < 4:
    print (nome[i])
    i = i + 1

nprocure = input('Nome a ser pesquisado na lista : ')

try:
  indice = nome.index(nprocure)
except ValueError:
  print ("O valor pesquisado nao foi encontrado")
else:
  print ("O valor foi encontrado : ", nome[indice], 'no indice ', indice)



# 3 – Crie uma lista de números ordenados, em seguida
# embaralhe os números da mesma.

numero = [ 1,2,3,4,5,6,7,8,9 ]
print("Lista Ordenada .....: ", numero)
random.shuffle(numero)
print("Lista Embaralhada ..: ", numero)

