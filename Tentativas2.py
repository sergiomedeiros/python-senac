from random import randint
print('Bem Vindo !!!!')
novo_jogo = True

while novo_jogo != False:
    numero_sorteado = randint(1,100)
    # print(numero_sorteado)
    contador = 1
    while True:
        chute = int (input("Chute um numero : "))
        if chute == numero_sorteado:
            print("Parabens, voce e foda.")
            break
        else:
            print("Alto" if chute > numero_sorteado else "Baixo")

        contador += 1


    print("Fim de Jogo!!!")
    print("Numero sorteado: " + str(numero_sorteado))
    print("Numero de chutado: " + str(chute))
    print("Numero de tentativas: " + str(contador))
    novo_jogo = int(input("Jogar novamente? 1 - Sim ou 0 - Não: "))
    
