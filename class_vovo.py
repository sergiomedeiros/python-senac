from class_pessoa import Pessoa

class Vovo(Pessoa):

    # O atributo foi identifica por nao esta sendo referenciado
    # no construtor
    nome=""

    # Valor None, para poder passar valor nulo.
    def __init__(self,nome=None, mae=None):
        super() .__init__(nome,mae)

    # sobrecarga do metodo da super classe
    def andar(self):
        print("Já sou bem grandinha, sei andar sozinha!")

    def idade(self, idade):
        self.idade = idade
        print("Eu tenho : ", idade , " anos.")
