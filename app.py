from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from tkinter.ttk import Treeview
from produto import Produto

        
class Inicio:
    def __init__(self, master):
        self.telaInicio = master
        self.telaInicio.geometry('300x200')
        self.telaInicio.title('Início')

        # Containers
        self.container1 = Frame(self.telaInicio)
        self.container1.pack(padx=50, pady=15) 
        self.container2 = Frame(self.telaInicio)
        self.container2.pack(padx=50, pady=4)
        self.container3 = Frame(self.telaInicio)
        self.container3.pack(padx=50, pady=8)
        
        # Widgets
        self.tituloLabel = Label(self.container1, text='Sistema de Estoque', font=BOLD)
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
        self.telaListaProdutos.title('Lista')

        # Containers
        self.container1 = Frame(self.telaListaProdutos)
        self.container1.pack(padx=50, pady=15)
        self.container2 = Frame(self.telaListaProdutos)
        self.container2.pack(padx=50, pady=4)
        self.container3 = Frame(self.telaListaProdutos)
        self.container3.pack(side=LEFT, padx=50, pady=10)
        self.container4 = Frame(self.telaListaProdutos)
        self.container4.pack(side=LEFT, padx=50, pady=10)
        self.container5 = Frame(self.telaListaProdutos)
        self.container5.pack(side=RIGHT, padx=50, pady=4)


        # Widgets
        self.tituloLabel = Label(self.container1, text='Lista de Produtos', font=BOLD)
        self.tituloLabel.pack()

        self.lista = Treeview(self.container2, columns=('produtoID', 'codigo', 'nome', 'preco', 'categoria'))
        self.lista.pack(side=LEFT)
        self.listaScroll = ttk.Scrollbar(self.container2, orient='vertical', command=self.lista.yview)
        self.listaScroll.pack(side=RIGHT, fill='y')
        self.lista.configure(height=25, yscrollcommand=self.listaScroll.set)

        self.lista.heading('#0', text='', anchor=CENTER)
        self.lista.heading('produtoID', text='produtoID', anchor=CENTER)
        self.lista.heading('codigo', text='Código', anchor=CENTER)
        self.lista.heading('nome', text='Nome', anchor=CENTER)
        self.lista.heading('preco', text='Preço', anchor=CENTER)
        self.lista.heading('categoria', text='Categoria', anchor=CENTER)

        self.lista.column('#0', width=0, stretch=NO)
        self.lista.column('produtoID', anchor=CENTER)
        self.lista.column('codigo', anchor=CENTER)
        self.lista.column('nome', anchor=CENTER)
        self.lista.column('preco', anchor=CENTER)
        self.lista.column('categoria', anchor=CENTER)

        produto = Produto()
        for i in produto.listar_produto():
            self.lista.insert('', 'end', values=i)

        self.buscar = Entry(self.container3, width=30)
        self.buscar.pack(side=LEFT, padx=2)
        self.buscarButton = Button(self.container3, text='Buscar', command=self.buscar_registro)
        self.buscarButton.pack(side=LEFT, padx=2)
        self.mostrarTodosButton = Button(self.container3, text='Mostrar Todos / Atualizar Lista', command=self.mostrar_todos)
        self.mostrarTodosButton.pack(side=LEFT)

        self.editarButton = Button(self.container4, text='Editar', command=self.opcao_editar)
        self.editarButton.pack(side=LEFT, padx=2)
        self.excluirButton = Button(self.container4, text='Excluir', command=self.deletar_registro)
        self.excluirButton.pack(side=RIGHT)

        self.voltarButton = Button(self.container5, text='Voltar', command=self.voltar)
        self.voltarButton.pack()

    def buscar_registro(self):
        produto = Produto()
        c = 0
        for i in produto.listar_produto():
            if self.buscar.get() == str(i[1]):
                if c == 0:
                    self.lista.delete(*self.lista.get_children())
                    c += 1
                self.lista.insert('', 'end', values=i)
            elif self.buscar.get().upper() == i[2].upper():
                if c == 0:
                    self.lista.delete(*self.lista.get_children())
                    c += 1
                self.lista.insert('', 'end', values=i)
            elif self.buscar.get().upper() == str(i[3]):
                if c == 0:
                    self.lista.delete(*self.lista.get_children())
                    c += 1
                self.lista.insert('', 'end', values=i)
            elif self.buscar.get().upper() == i[4].upper():
                if c == 0:
                    self.lista.delete(*self.lista.get_children())
                    c += 1
                self.lista.insert('', 'end', values=i)
        self.lista.pack()

    def opcao_editar(self):
        try:
            selecionado = self.lista.selection()[0]
            valores = self.lista.item(selecionado, 'values')
            self.novaTela = Toplevel(self.telaListaProdutos)
            EdicaoProduto(self.novaTela, self.telaListaProdutos, valores)
        except:
            messagebox.showerror('Erro', 'Selecione um registro a ser editado.')
        
        self.mostrar_todos()

    def deletar_registro(self):
        produto = Produto()
        try:
            selecionado = self.lista.selection()[0]
            valores = self.lista.item(selecionado, 'values')
            id = valores[0]
            resposta = messagebox.askyesno('Cuidado', 'Deseja deletar esse registro pra sempre?')
            if resposta:
                produto.deletar_produto(id)
                self.lista.delete(selecionado)
        except:
            messagebox.showerror('Erro', 'Selecione um registro a ser deletado.')

    def mostrar_todos(self):
        self.lista.delete(*self.lista.get_children())
        produto = Produto()
        for i in produto.listar_produto():
            self.lista.insert('', 'end', values=i)
        self.lista.pack()

    def voltar(self):
        self.origem.deiconify() 
        self.telaListaProdutos.destroy()

class CadastroProduto:
    def __init__(self, master, root):
        self.origem = root
        self.telaCadastroProdutos = master
        self.telaCadastroProdutos.title('Cadastro')

        # Containers
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

        # Widgets
        self.tituloLabel = Label(self.container1, text='Cadastro de Produtos', font=BOLD)
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

        self.categorias = [
            'Alimentos',
            'Eletrônicos',
            'Limpeza'
            'Roupas',
            'Papelaria',
        ]

        self.selecionado = StringVar()
        self.selecionado.set(self.categorias[0])
        self.categoriaLabel = Label(self.container5, text='Categoria', width=8)
        self.categoriaLabel.pack(side=LEFT)
        self.categoria = OptionMenu(self.container5, self.selecionado, *self.categorias)
        self.categoria.pack()

        self.cadastrarButton = Button(self.container6, text='Cadastrar', command=self.cadastrar_produto)
        self.cadastrarButton.pack()

        self.voltarButton = Button(self.container7, text='Voltar', command=self.voltar)
        self.voltarButton.pack()

    def cadastrar_produto(self):
        produto = Produto()
        produto.codigo = self.codigo.get()
        produto.nome = self.nome.get()
        if ',' in self.preco.get():
            a = self.preco.get().replace(',', '.')
            produto.preco = a
        else:
            produto.preco = self.preco.get()
        produto.categoria = self.selecionado.get()

        if (produto.codigo and produto.nome and produto.preco):
            produto.cadastrar_produto()
            messagebox.showinfo('Sucesso', 'Produto cadastrado com sucesso.')

            self.codigo.delete(0, END)
            self.nome.delete(0, END)
            self.preco.delete(0, END)
        else:
            messagebox.showwarning('Aviso', 'Nenhum campo pode estar vazio.')

    def voltar(self):
        self.origem.deiconify()
        self.telaCadastroProdutos.destroy()

class EdicaoProduto:
    def __init__(self, master, root, valores):
        self.origem = root
        self.telaEdicao = master
        self.telaEdicao.title('Editar')
        self.valores = valores
        
        self.container1 = Frame(self.telaEdicao)
        self.container1.pack(padx=50, pady=15)
        self.container2 = Frame(self.telaEdicao)
        self.container2.pack(padx=50, pady=4)
        self.container3 = Frame(self.telaEdicao)
        self.container3.pack(padx=50, pady=4)
        self.container4 = Frame(self.telaEdicao)
        self.container4.pack(padx=50, pady=4)
        self.container5 = Frame(self.telaEdicao)
        self.container5.pack(padx=50, pady=4)
        self.container6 = Frame(self.telaEdicao)
        self.container6.pack(padx=50, pady=15)

        self.tituloLabel = Label(self.container1, text='Alteração dos Registros', font=BOLD)
        self.tituloLabel.pack()

        self.codigoEditarLabel = Label(self.container2, text='Código', width=8)
        self.codigoEditarLabel.pack(side=LEFT)
        self.codigoEditar = Entry(self.container2, width=30)
        self.codigoEditar.insert(0, self.valores[1])
        self.codigoEditar.pack(side=LEFT)

        self.nomeEditarLabel = Label(self.container3, text='Nome', width=8)
        self.nomeEditarLabel.pack(side=LEFT)
        self.nomeEditar = Entry(self.container3, width=30)
        self.nomeEditar.insert(0, self.valores[2])
        self.nomeEditar.pack(side=LEFT)

        self.precoEditarLabel = Label(self.container4, text='Preço', width=8)
        self.precoEditarLabel.pack(side=LEFT)
        self.precoEditar = Entry(self.container4, width=30)
        self.precoEditar.insert(0, self.valores[3])
        self.precoEditar.pack(side=LEFT)

        self.categorias = [
            'Alimentos',
            'Eletrônicos',
            'Limpeza',
            'Roupas',
            'Papelaria',
        ]

        self.selecionado = StringVar()
        self.selecionado.set(self.valores[4])

        self.categoriaEditarLabel = Label(self.container5, text='Categoria', width=8)
        self.categoriaEditarLabel.pack(side=LEFT)
        self.categoriaEditar = OptionMenu(self.container5, self.selecionado, *self.categorias)
        self.categoriaEditar.pack()

        self.confirmarEditarButton = Button(self.container6, text='Confirmar', command=self.editar_registro)
        self.confirmarEditarButton.pack()

    def editar_registro(self):
        produto = Produto()
        produto.produtoID = self.valores[0]
        produto.codigo = self.codigoEditar.get()
        produto.nome = self.nomeEditar.get()
        if ',' in self.precoEditar.get():
            a = self.precoEditar.get().replace(',', '.')
            produto.preco = a
        else:
            produto.preco = self.precoEditar.get()
            produto.categoria = self.selecionado.get()

        if (produto.codigo and produto.nome and produto.preco):
            produto.editar_produto()
            messagebox.showinfo('Sucesso', 'Produto editado com sucesso.')
            self.telaEdicao.destroy()
        else:
            messagebox.showwarning('Aviso', 'Nenhum campo pode estar vazio.')

root = Tk()
Inicio(root)
root.mainloop()

