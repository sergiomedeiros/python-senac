class Pessoa(object):
    nome=""
    idade = 0
    pai = " "

    # Metodo construtor
    def __init__(self, nome):
        self.nome = nome

    # Definindo metodo
    def andar(self):
        print("A pessoa esta andando .....")

              
# Instanciamos o objeto 
#p = Pessoa()
# Instanciando apos a criaçao do construtor
p = Pessoa("Sergio Medeiros")
# Definimos o valor do atributo nome
# p.nome = "Sergio Medeiros"
# Definimos o valor do atributo idade
p.idade = 38

# Faz a impressao dos valores dos atributos
print(p.nome)
print(p.idade)

print(p.nome, 'tem ', p.idade, 'anos ')
p.andar()
