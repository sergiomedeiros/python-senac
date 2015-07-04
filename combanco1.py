
import MySQLdb

con = MySQLdb.connect(host='localhost', user='root', passwd='sergio',db='senac')

x = con.cursor()

"""
x.execute("INSERT INTO alunos (nomealuno, curso, turma, turno) VALUES ('Marcos Antonio','Python','SE','TARDE');")
x.execute("INSERT INTO alunos (nomealuno, curso, turma, turno) VALUES ('Rogeio','Python','SE','TARDE');")
x.execute("INSERT INTO alunos (nomealuno, curso, turma, turno) VALUES ('Marcos Antonio','Python','SERGYGY','MANHA');")
con.commit()


# Consultar um registro no banco
SELECT * FROM alunos where nome_aluno = "Sergio";



# Deletar um registro no banco
DELETE FROM alunos WHERE nome_aluno = "Sergio";

# Alterar dados no banco
UPDATE alunos SET nome_aluno="Fabricio" WHERE nome_aluno = "Sergio";

"""

x.execute("""SELECT * FROM alunos;""")
print 'Listando Alunos :'
for linha in x.fetchall():
    print linha[0],'\n' # valor da primeira coluna

con.close()
