import sqlite3


class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('estoque.db')
        self.criar_tabela()

    def criar_tabela(self):
        cursor = self.conexao.cursor()

        cursor.execute('''
            CREATE table IF NOT EXISTS produtos (
                produtoID INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo INT NOT NULL,
                nome VARCHAR(100),
                preco DECIMAL,
                categoria VARCHAR(100))''')
        self.conexao.commit()
        cursor.close()