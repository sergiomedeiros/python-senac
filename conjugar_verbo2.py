
#Primeiro criamos listas com as terminações de verbos regulares


# criar funcao de conexao

    
    

import sqlite3
db = sqlite3.connect("senac.db")
cursor = db.cursor()

pessoas   = ['Eu', 'Tu', 'Ele', 'Nós', 'Vós', 'Eles']
conjuga_ar= ['o', 'as', 'a', 'amos', 'ais', 'am']
conjuga_er= ['o', 'es', 'e', 'emos', 'eis', 'em']
conjuga_ir= ['o', 'es', 'e', 'imos', 'is', 'em']

print('Vamos Brincar de Conjugar !!!!')
novo_verbo = True

while novo_verbo != False:
    
    #a seguir, pedimos que o usuário informe o verbo
    usuario = input('Digite o nome do usuario : ')
    verbo = input('Digite o infitivode um verbo regular: ')
    #separa a terminação do verbo
    termina_em= verbo[-2:]
    #agora, de acordo com a terminação do verbo, conjuga apropriadamente

    if termina_em== 'ar':
        for i in range(6): #repete seis vezes, percorrendo a lista
            print(pessoas[i]+ ' ' + verbo[:-2]+conjuga_ar[i])

    elif termina_em== 'er':
        for i in range(6): #repete seis vezes, percorrendo a lista
            print(pessoas[i]+ ' ' + verbo[:-2]+conjuga_er[i])

    elif termina_em== 'ir':
        for i in range(6): #repete seis vezes, percorrendo a lista
            print(pessoas[i]+ ' ' + verbo[:-2]+conjuga_ir[i])

    else:
        print("Tem certeza que " +verbo.upper()+ " é um verbo regular?")

    #sql = "SELECT count(*) FROM verbo_conjugar where verbo = '%s' " % verbo
    sql = "SELECT count(*) FROM verbo_conjugar"
    print(sql)
    cursor.execute(sql)
    cursor.execute("""SELECT * FROM verbo_conjugar;""")
    for linha in cursor.fetchall():
        print (linha[0],' - ', linha[1],'\n') # valor da primeira coluna

        
    print(cursor.fetchall())
    cursor.execute(sql)
    qtdconjuga = cursor.rowcount
    print('Conta ',qtdconjuga)
    
    """
    qtdconjuga = cursor.execute(sql)
    print(qtdconjuga)
    sql = "INSERT INTO verbo_conjugar (verbo, qt_vezes) VALUES ('%s', %d)" % (verbo,qtdconjuga)
    try:
        #execute the sql command
        cursor.execute(sql)
        #commit your changes to the db
        db.commit()
    except:
        #rollback on error
        db.rollback()

    sql = "SELECT count(*) FROM usuario where nome = '%s' " %usuario
    qtdusuario = cursor.execute(sql)
    if qtdusuario == 0:
        sql = "INSERT INTO usuario (nome) VALUES ('%s'" % usuario
        try:
            #execute the sql command
            cursor.execute(sql)
            #commit your changes to the db
            db.commit()
        except:
            #rollback on error
            db.rollback()
       """ 
   
    novo_verbo = int(input("Conjungar outro verbo ? 1 - Sim ou 0 - Não: "))




cursor.execute("""SELECT * FROM verbo_conjugar;""")
for linha in cursor.fetchall():
    print (linha[0],' - ', linha[1],'\n') # valor da primeira coluna


db.close()
