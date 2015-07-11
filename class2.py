class Pessoa (object):
    nome = ""
    idade = 0
    cpf = ""

    def diz_nome(self):
        return self.nome

    def diz_idade(self):
        return self.idade


cliente = Pessoa()
cliente.nome = "Eduardo Basilio"
cliente.idade = 34
cliente.cpf ="12345678901"

cliente.diz_idade()
cliente.diz_nome()

