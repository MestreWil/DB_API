import sqlite3
from pathlib import Path

# Criando o caminho para o arquivo, do sqlite

ROOT_PATH = Path(__file__).parent

# Criando banco de dados sqlite com o ROOT_PATH
conexao = sqlite3.connect(ROOT_PATH / "clientes.sqlite")

# Usando o cursor para usar os comandos sql
cursor = conexao.cursor()

# Usando o .execute para criar a tabela clientes dentro do banco de dados clientes
# cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))')

data = ("William", "will@gmail.com")
# obs: NA HORA DE INSERIR DADOS É UMA BOA PRATICA DE SEGURANÇA 
cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?);", data )
conexao.commit()