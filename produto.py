from sqlite3 import Cursor
from banco import Banco


class Produto(object):
    def __init__(self, produtoID='', codigo='', nome='', preco='', categoria=''):
        self.produtoID = produtoID
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    def cadastrar_produto(self):
        banco = Banco()
        try:
            cursor = banco.conexao.cursor()

            cursor.execute(f'INSERT INTO produtos (codigo, nome, preco, categoria) VALUES ("{self.codigo}", "{self.nome}", "{self.preco}", "{self.categoria}")')

            banco.conexao.commit()
            cursor.close()
            return 'Produto inserido com sucesso!'
        except:
            return 'Ocorreu um erro na inserção do produto.'

    def listar_produto(self):
        banco = Banco()
        cursor = banco.conexao.cursor()

        cursor.execute(f'SELECT * FROM produtos')
        resultado = cursor.fetchall()
        cursor.close()
        return resultado