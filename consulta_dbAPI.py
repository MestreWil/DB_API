import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "clientes.sqlite")

cursor = conexao.cursor()

def recuperar_cliente(cursor, id):
  cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
  return cursor.fetchone()

# o cursor retorna um iteravel, uma estrutura que precisamos passar linha a linha
def listar_clientes(cursor):
  return cursor.execute("SELECT * FROM clientes")

# O row_factory retorna um dicionario, chave = valor, da consulta sql
def recuperar_cliente_row(cursor, id):
  cursor.row_factory = sqlite3.Row
  cursor.execute('SELECT * FROM clientes WHERE id=?', (id,))
  return cursor.fetchone()


# cliente = recuperar_cliente(cursor, 2)
# print(cliente)

# tupla_clientes = listar_clientes(cursor)

#for cliente in tupla_clientes:
#  print(cliente)

dict_clientes = recuperar_cliente_row(cursor, 2)
print(dict_clientes["nome"])