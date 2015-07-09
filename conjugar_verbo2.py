
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

   
    sql = "INSERT INTO conjugar (nome, verbo, qt_vezes) VALUES ('%s','%s', 1)" % (usuario, verbo)
    try:
        #execute the sql command
        cursor.execute(sql)
        #commit your changes to the db
        db.commit()
    except:
        #rollback on error
        db.rollback()
   
    novo_verbo = int(input("Conjungar outro verbo ? 1 - Sim ou 0 - Não: "))



cursor.execute("""SELECT count(*) FROM conjugar;""")
print ('Listando Usuarios ( ', cursor.fetchall() , ' ) :')
cursor.execute("""SELECT * FROM conjugar;""")
for linha in cursor.fetchall():
    print (linha[0],' - ', linha[1],'\n') # valor da primeira coluna


db.close()
