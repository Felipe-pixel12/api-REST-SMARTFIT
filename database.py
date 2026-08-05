import sqlite3

DATABASE = "alunos.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabela():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS alunos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            cpf TEXT NOT NULL,
            idade INTEGER NOT NULL
        )
    """)

    conn.comit()
    conn.close()
    