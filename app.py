from ctypes import WinDLL
from tkinter import *

from setuptools import Command

        
class Inicio:
    def __init__(self, master):
        self.telaInicio = master
        self.telaInicio.title('Início')

        # Containers
        self.container1 = Frame(self.telaInicio)
        self.container1.pack(padx=50, pady=15) 
        self.container2 = Frame(self.telaInicio)
        self.container2.pack(padx=50, pady=4)
        self.container3 = Frame(self.telaInicio)
        self.container3.pack(padx=50, pady=4)
        
        # Widgets
        self.tituloLabel = Label(self.container1, text='Sistema de Estoque')
        self.tituloLabel.pack() 

        self.listaButton = Button(self.container2, text='Lista de Produtos', command=self.opcao_listar)
        self.listaButton.pack()

        self.cadastroButton = Button(self.container3, text='Cadastro de Produtos', command=self.opcao_cadastrar)
        self.cadastroButton.pack()
        
    def opcao_listar(self):
        self.telaInicio.withdraw()
        self.novaTela = Toplevel(self.telaInicio)
        ListaProduto(self.novaTela, self.telaInicio)

    def opcao_cadastrar(self):
        self.telaInicio.withdraw()
        self.novaTela = Toplevel(self.telaInicio)
        CadastroProduto(self.novaTela, self.telaInicio)

class ListaProduto:
    def __init__(self, master, root):
        self.origem = root
        self.telaListaProdutos = master
        self.telaListaProdutos.title('Lista de Produtos')
        
        # Containers
        self.container1 = Frame(self.telaListaProdutos)
        self.container1.pack(padx=50, pady=15)
        self.container2 = Frame(self.telaListaProdutos)
        self.container2.pack(padx=50, pady=4)

        # Widgets
        self.tituloLabel = Label(self.container1, text='Lista de Produtos')
        self.tituloLabel.pack()

        self.voltarButton = Button(self.container1, text='Voltar', command=self.voltar)
        self.voltarButton.pack()

    def voltar(self):
        self.origem.deiconify()
        self.telaListaProdutos.destroy()

class CadastroProduto:
    def __init__(self, master, root):
        self.origem = root
        self.telaCadastroProdutos = master
        self.telaCadastroProdutos.title('Cadastro de Produtos')

        self.container1 = Frame(self.telaCadastroProdutos)
        self.container1.pack(padx=50, pady=15)
        self.container2 = Frame(self.telaCadastroProdutos)
        self.container2.pack(padx=50, pady=4)
        self.container3 = Frame(self.telaCadastroProdutos)
        self.container3.pack(padx=50, pady=4)
        self.container4 = Frame(self.telaCadastroProdutos)
        self.container4.pack(padx=50, pady=4)
        self.container5 = Frame(self.telaCadastroProdutos)
        self.container5.pack(padx=50, pady=4)
        self.container6 = Frame(self.telaCadastroProdutos)
        self.container6.pack(padx=50, pady=4)
        self.container7 = Frame(self.telaCadastroProdutos)
        self.container7.pack(side=RIGHT, padx=50, pady=15)

        self.tituloLabel = Label(self.container1, text='Cadastro de Produtos')
        self.tituloLabel.pack()

        self.codigoLabel = Label(self.container2, text='Código', width=8)
        self.codigoLabel.pack(side=LEFT)
        self.codigo = Entry(self.container2, width=30)
        self.codigo.pack()

        self.nomeLabel = Label(self.container3, text='Nome', width=8)
        self.nomeLabel.pack(side=LEFT)
        self.nome = Entry(self.container3, width=30)
        self.nome.pack()

        self.precoLabel = Label(self.container4, text='Preço', width=8)
        self.precoLabel.pack(side=LEFT)
        self.preco = Entry(self.container4, width=30)
        self.preco.pack()

        categorias = [
            'Alimentos',
            'Eletrônicos',
            'Roupas',
            'Papelaria',
        ]

        self.selecionado = StringVar()
        self.selecionado.set(categorias[0])
        self.categoriaLabel = Label(self.container5, text='Categoria', width=8)
        self.categoriaLabel.pack(side=LEFT)
        self.categoria = OptionMenu(self.container5, self.selecionado, *categorias)
        self.categoria.pack()

        self.cadastrarButton = Button(self.container6, text='Cadastrar', command=self.cadastrar_produto)
        self.cadastrarButton.pack()

        self.voltarButton = Button(self.container7, text='Voltar', command=self.voltar)
        self.voltarButton.pack()

    def cadastrar_produto(self):
        pass


    def voltar(self):
        self.origem.deiconify()
        self.telaCadastroProdutos.destroy()

root = Tk()
Inicio(root)
root.mainloop()