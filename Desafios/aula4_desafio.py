    

class Exerciooo1(object):
    # 1 - Crie um programa que calcule valores reais em dolares
    # Definindo metodo
    def CalcRealDolar(self):
        valord = float(input('Qual a cotação atual do dólar em reais? '))
        valorr = float(input('Qual valore em real que deseja converter para dolar ? '))
        total = valorr / valord
        print ('Seu valor em dólares fica: U$ %.4f \n' %total)     #% mascara e 2f duas casas decimais.
        
    # 2 - Converta em pes a altura de uma pessoa;
    def PesMetro(self):
        valor = float (input("Informe a altura da pessoa : "))
        print('Altura em Pes ..: ', valor*3.2808399)

    # 3 - Calcule a capacidade maxima de pessoas dentro de uma sala
    def CapSala(self):
        valor = float (input("Informe a area quantrada da sala : "))
        print('Capacidade maxima de pessoas em pe e ..: ', (valor*0.88)*0.8)
        

#------------------------- Execucao (inicio)
continua = True
while continua != False:
    print ("Bem vindo ao orientacao a objetos!")
    print( "Digite o número da opção desejada: \n",
           "1 - Crie um programa que calcule valores reais em dolares \n",
           "2 - Converta em pes a altura de uma pessoa \n",
           "3 - Calcule a capacidade maxima de pessoas dentro de uma sala \n",
           "4 - Sair")

    opcao = int (input("Digite a opcao : "))

    p = Exerciooo1()

    if opcao == 1:
        p.CalcRealDolar()
    elif opcao == 2:
        p.PesMetro()
    elif opcao == 3:
        p.CapSala()
    else:
        continua = False

#------------------------- Execucao (fim)
