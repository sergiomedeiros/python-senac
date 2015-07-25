dialogo = open('dialogo.txt')
dialogo.seek(0)  #informar em que linha vai inicia a leitura.
for linha in dialogo:
    print(linha,end='')   #end='' para evitar a quebra de linha

dialogo.close()
   
