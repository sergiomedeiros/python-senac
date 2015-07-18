from class_pessoa import Pessoa
from class_pessoa_bb import BB
from class_vovo import Vovo

# Instanciando um objeto do tipo BB
bb1 = BB('Anne Isabel','Bel')

# Imprime o BB criado ..
print("Nome : ", bb1.nome)
print("Mae : ", bb1.mae)

# Metodo definido na super classe Pessoa
bb1.andar()

# Metodo definido na sub-classe BB
bb1.bicicleta()

# Metodo chorar da super classe
bb1.chorar()

print("-----------------P E S S O A--------------------------")
# Instanciando um objeto tipo Pessoa
p1 = Pessoa("Joao Miguel","Emanuela Carvalho")

# Imprime a pessoa criada ...
print("Nome : " , p1.nome)
print("Mae : ", p1.mae)

# Metodo definido na propria classe
p1.andar()
p1.chorar()

# Isso vai da merda federal !!! :(
#p1.bicicleta()   # Esse metodo esta definido na sub-classe, por isso nao funciona

print("-----------------V O V O--------------------------")
# Instanciando uma nova vovo
vo = Vovo()
# Setando o nome da voco
vo.nome = "Maria do Amporo"
# Imprime o noma da vovo
print(vo.nome)
# Chamada ao metodo da sub-classe vovo
vo.idade(59)
# Acessando metodo sobrescrito da super classe
vo.andar()


