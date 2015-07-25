dialogo = open('dialogo.txt')
dialogo.seek(0)  #informar em que linha vai inicia a leitura.
for linha in dialogo:
    ator, fala = linha.slpit(':')
    print(ator,end='')
    print(' diz ', end='')
    print(fala,end='')

dialogo.close()
