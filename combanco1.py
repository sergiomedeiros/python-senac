
import MySQLdb

con = MySQLdb.connect(host='localhost', user='root', passwd='sergio',db='senac')

x = con.cursor()

x.execute("INSERT INTO alunos (nomealuno, curso, turma, turno) VALUES ('Marcos Antonio','Python','SE','TARDE');")
x.execute("INSERT INTO alunos (nomealuno, curso, turma, turno) VALUES ('Rogeio','Python','SE','TARDE');")
x.execute("INSERT INTO alunos (nomealuno, curso, turma, turno) VALUES ('Marcos Antonio','Python','SERGYGY','MANHA');")
con.commit()

x.execute("""SELECT * FROM alunos;""")
print x.fetchall()
con.close()
