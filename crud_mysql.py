"""
Exibindo Curso Python e Django - Aula 2.pdf…
Desafios
1 - Criar um CRUD usando o Mysql
"""
# Importe o modulo do MySQL 
import MySQLdb

# Crie uma conexão com o banco
con = MySQLdb.connect(host='localhost', user='root', passwd='',db='testepy')

# Pegue o cursor da conexao
c = con.cursor()



# Fechando a conexao com o banco
con.close()
