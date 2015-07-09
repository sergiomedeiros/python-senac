
import sqlite3
db = sqlite3.connect("senac.db")



cursor = db.cursor()

cursor.execute("""SELECT count(*) FROM conjugar;""")
print(cursor.fetchone())
db.close()


#cursor.execute("""CREATE TABLE conjugar (id integer primary key autoincrement,nome varchar(100) not null,verbo varchar(40) not null,qt_vezes numeric(3) not null )""")
#usuario='sergio medeiros'
#verbo="ver"
#sql = "INSERT INTO conjugar (nome, verbo, qt_vezes) VALUES ('%s','%s', 1)" % (usuario, verbo)
#print(sql)

#cursor.execute(sql)

#cursor.execute("""SELECT count(*) FROM conjugar;""")
#print(cursor.fetchone())
#cursor.execute("""SELECT * FROM conjugar;""")
#print(cursor.fetchone())
#db.commit()

#print ('Listando Usuarios :')
#for linha in cursor.fetchall():
#    print (linha[0],' - ', linha[1],' - ',linha[2], '\n') # valor da primeira coluna


#cursor.execute("""delete FROM conjugar""")



