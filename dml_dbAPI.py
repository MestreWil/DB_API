import sqlite3
from pathlib import Path

# Criando o caminho para o arquivo, do sqlite

ROOT_PATH = Path(__file__).parent

# Criando banco de dados sqlite com o ROOT_PATH
conexao = sqlite3.connect(ROOT_PATH / "clientes.sqlite")

# Usando o cursor para usar os comandos sql
cursor = conexao.cursor()

# Usando o .execute para criar a tabela clientes dentro do banco de dados clientes
# 


# obs: NA HORA DE INSERIR DADOS É UMA BOA PRATICA DE SEGURANÇA 



def criar_tabela(conexao, cursor):
  cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')
  
def inserir_registro(conexao, cursor, nome, email):
  data = (nome, email)
  cursor.execute("INSERT INTO clientes (nome, email, id) VALUES (?, ?);", data )
  conexao.commit()
  
def atualizar_registro(conexao, cursor, nome, email, id):
  data = (nome, email, id)
  cursor.execute('UPDATE clientes SET nome=?, email=? WHERE id=?;', data)
  conexao.commit()
  
# inserir_registro(conexao, cursor, "Mestre Will", "mestre@gmail.com")
# inserir_registro(conexao, cursor, "Nat Gostosa", "nat_saborosa@gmail.com", 1)

def excluir_registro(conexao, cursor, id):
  data = (id,)
  cursor.execute("DELETE FROM clientes WHERE id=?;", data)
  conexao.commit()
  
# excluir_registro(conexao, cursor, 1)

def inserir_muitos(conexao, cursor, dados):
  cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
  conexao.commit()
  
dados = [
  ("Comedor386", "comedor@hotmail.com"),
  ("Luana TARADA", "safadinha69@gmail.com"), 
  ("Chapado de POA", "marihuaja@gmail.com")
]
inserir_muitos(conexao, cursor, dados)