import sqlite3

try:
   con = sqlite3.Connection("meu_banco.bd")

   cur = con.cursor()

   cur.execute("DROP TABLE pessoa")

   cur.execute("CREATE TABLE pessoa(id_pessoa  INTEGER PRIMARY KEY ASC AUTOINCREMENT,"+
                "nome VARCHAR(400),"+
                "idade INTEGER,"+
                "cpf VARCHAR(15))")

   cur.execute("CREATE TABLE consulta(id PRIMARY KEY ASC AUTOINCREMENT,"+
                "data_consulta DATETIME,"+
                "horario DATETIME,"+
                "id_pessoa INTEGER"+
                "FOREING KEY (id_pessoa) REFERENCES pessoa(id))")
   
   cur.execute("SELECT nome, data_consulta FROM pessoa, consulta WHERE pessoa.id_pessoa = %d" % 1)
   res = cur.fetchone()
   print(res)
   con.commit()
   cur.close()
   con.close()
except ConnectionResetError as c:
   print('Erro de conexão com o banco.')