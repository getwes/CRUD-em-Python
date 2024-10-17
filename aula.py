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
nome_produto = "todynho"
valor =6
comando = f'UPDATE vendas SET VALOR = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()# edita o banco de dados

#finalizar a conexao e o cursor
cursor.close()
conexao.close()

#create
#nome_produto = "todynho"
#valor = 3
#comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
#cursor.execute(comando)
#conexao.commit()# edita o banco de dados
#resultado = cursor.fetchall()#ler o banco de dados

#read
#comando = f'SELECT * FROM vendas'
#cursor.execute(comando)
#resultado = cursor.fetchall()#ler o banco de dados
#print(resultado)

#update
nome_produto = "todynho"
valor =6
comando = f'UPDATE vendas SET VALOR = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()# edita o banco de dados