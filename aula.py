import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Wes170702',
    database='bdyoutube',
)
#cursor é quem faz a conexao com o banco de dados
cursor = conexao.cursor()


#crud



#finalizar a conexao e o cursor
cursor.close()
conexao.close()
