import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="tallys",
    password="teste123",
    database="infecteds"
)
print(db)
cursor = db.cursor()

print("RE gISTRO de C O VI D dezenove.1")
print("\n\n\n")

option = input("0 - EXIBIR DADOS\n1 - Cadastrar infectado\n2 - Deletar Infectado\n3 - Atualizar infectado\n-----------------\nPLANOS DE SAÚDE\n"+
               "5 - Cadastrar plano\n6 - Excluir plano\n7 - Atualizar pagamento\n")


if option == "0":
    dados = input("\n1 - INFECTADOS\n2 - PLANOS\n3 - Busca simples em infectados\n4 - Listar devedores\n").upper()
    
    if dados == "1":
        cursor.execute("SELECT * FROM infecteds")
        result = cursor.fetchall()
        for item in result:
            print(item)

    if dados == "2":
        cursor.execute("SELECT * FROM plano")
        result = cursor.fetchall()
        for item in result:
            print(item)

    if dados == "3":
        nome = input("Buscar infectado de nome\n").upper()
        cursor.execute("SELECT * FROM infecteds WHERE name ='"+nome+"'")
        result = cursor.fetchall()
        
        for item in result:
            print(item)
            
    if dados == "4":
        #INNER JOIN
        print('ok')

if option == "1":
    nome = input("Nome paciente\n").upper()
    plano = input("Plano paciente\n").upper()
    
    cursor.execute("INSERT INTO infecteds (name, plano) VALUES (%s, %s)", (nome,plano))

if option == "2":
    nome = input("Nome paciente\n").upper()
    
    cursor.execute("DELETE FROM infecteds WHERE name ='"+nome+"'")
    
if option == "3":
    nomeanterior = input("Infectado para ser atualizado\n")
    nome = input("Novo nome\n").upper()
    plano = input("Novo plano\n").upper()
    
    cursor.execute("UPDATE infecteds SET name = %s WHERE name = %s",(nome, nomeanterior))
    cursor.execute("UPDATE infecteds SET plano = %s WHERE name = %s", (plano, nomeanterior))
    cursor.execute("UPDATE plano SET nome = %s WHERE name = %s", (nome, nomeanterior))
    
        
if option == "4":
    busca = input("1 - Busca simples\n2 - Listar devedores\n")
    
    if busca == "1":
        nome = input("Buscar infectado de nome\n").upper()
        cursor.execute("SELECT * FROM infecteds WHERE name ='"+nome+"'")
        result = cursor.fetchall()
        
        for item in result:
            print(item)
    

    
if option == "5":
    plano = input("Nome do plano\n").upper()
    paciente = input("Nome do paciente (opcional)\n").upper()
    pago = input("Pago? S/N\n").upper()
    cursor.execute('INSERT INTO plano (name, paciente, pago) VALUES (%s, %s, %s)', (plano, paciente, True if pago == "S" else False))

    
if option == "6":
    plano = input("Excluir plano de nome\n").upper()
    
    cursor.execute('DELETE FROM plano WHERE NAME = ''+plano+''')

if option == "7":
    nome = input("\nAtualizar pagamendo no plano do infectado de nome\n")
    pago = input("Pago? S/n").upper()
    cursor.execute("UPDATE plano SET pago = %s WHERE name = %s",(True if pago == "S" else False, nome))


db.commit()