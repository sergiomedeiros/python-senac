# Realiza a importaçao da class Pessoa    
# Apos o from, informar o nome do arquivo.py, e se necessario o caminho absoluto
# Apos o import o nome da class
from class_pessoa import Pessoa

# Herdamos da classe Pessoa
class BB(Pessoa):
    def __init__(self, nome, mae):
        print("Método construtor de sub classe")
        # Acessa o metodo construtor da super classe
        super().__init__(nome, mae)
        self.nome = nome
        self.mae  = mae

    # Especializaçao da classe
    def bicicleta(self):
        print("Agora aprendendo a pedalar ...")
