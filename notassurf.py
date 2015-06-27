f = open("surf.txt","r")
notas = {}   # Cria um dicionario

for linha in f:
    nome, pontos = linha.split()    # os dados da linha as variavel
    notas[float(pontos)] = nome     # povoando o dicionario

f.close()
for nota in sorted(notas,reverse=True):
    print("%s tem %4.2f" %(notas[nota],nota))

# Numeros fload %caracte.decimalf
