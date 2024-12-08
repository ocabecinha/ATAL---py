import livro
import tkinter as tk
from tkinter import simpledialog, messagebox



lista = livro.metodos() #cria uma variel que vai chamar os metodos de livro
def adicionarLivro(): #função criada para adicionar o titulo, autor e ano na interface
    def salvar_livro():
        titulo = entry_titulo.get()
        autor = entry_autor.get()
        ano = entry_ano.get()
        if titulo and autor and ano:
            lista.adicionar_um_livro(titulo, autor, ano)
            add_window.destroy()
        else:
            messagebox.showwarning("Aviso", "Por favor, preencha todos os campos.")

    add_window = tk.Toplevel()#
    add_window.title("Adicionar Livro")
    add_window.geometry("300x300")

    tk.Label(add_window, text="Título:").pack(pady=5)
    entry_titulo = tk.Entry(add_window, width=30)
    entry_titulo.pack(pady=5)

    tk.Label(add_window, text="Autor:").pack(pady=5)
    entry_autor = tk.Entry(add_window, width=30)
    entry_autor.pack(pady=5)

    tk.Label(add_window, text="Ano de Publicação:").pack(pady=5)
    entry_ano = tk.Entry(add_window, width=30)
    entry_ano.pack(pady=5)

    tk.Button(add_window, text="Salvar", command=salvar_livro, width=20, bg="#4CAF50", fg="white").pack(pady=10)
    tk.Button(add_window, text="Cancelar", command=add_window.destroy, width=20, bg="#ff6666", fg="white").pack(pady=5)
def listarLivros(): #função criada para listar os livros que foram adicionado na lista

    list_window = tk.Toplevel()
    list_window.title("Lista de Livros")
    list_window.geometry("400x300")


    livros_info = lista.listar_livros()
    text_widget = tk.Text(list_window, wrap="word", width=50, height=15)
    text_widget.insert("1.0", livros_info )  # Insere o texto no widget
    text_widget.configure(state="disabled")  # Desabilita edição para o usuário
    text_widget.pack(padx=10, pady=10)
    btn_fechar = tk.Button(list_window, text="Fechar", command=list_window.destroy)
    btn_fechar.pack(pady=5)


def buscarLivroPorAutor(self):  #função criada para buscar o livro na lista
    def procurar_livro():
        autor = entry_autor.get() #recebe o input do usuario
        if autor:
            livro = lista.buscarLivroPorAutor(autor) #passa o input do usuario como parametro da busca
            if livro:
                livros_sugeridos = self.trie.search(autor)
                for livro in livros_sugeridos:
                    messagebox.showinfo("Livro Encontrado", f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publicacao}")
            else:
                messagebox.showinfo("Não Encontrado", "Livro não encontrado.")
            search_window.destroy()

    search_window = tk.Toplevel()#
    search_window.title("Buscar Livro")
    search_window.geometry("300x150")

    tk.Label(search_window, text="Título:").pack(pady=5)
    entry_autor = tk.Entry(search_window, width=30)
    entry_autor.pack(pady=5)

    tk.Button(search_window, text="Buscar", command=procurar_livro, width=20, bg="#4CAF50", fg="white").pack(pady=10)
    tk.Button(search_window, text="Cancelar", command=search_window.destroy, width=20, bg="#ff6666", fg="white").pack(pady=5)


def ordenarLivros():
    root = tk.Tk() #confesso que dei uma roubada no GPT pra fazer essa interface grafica, não ia perder meu tempo fazendo GUI
    root.title("Gerenciador de livros")
    root.geometry("400x300")
    root.configure(bg="#f5f5f5")

    frame = tk.Frame(root, bg="#f5f5f5")
    frame.pack(pady=20)

    #titulo
    titulo_label = tk.Label(frame, text="Ordenação dos livros", font=("Helvetica", 16, "bold"), bg="#f5f5f5")
    titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

    botoes = [
        ("Ordenar por titulo", "OrdenarTitulo"),#primeiro parametro é o texto do botão, e o segundo parametro é o comando de ação
        ("Ordenar por autor", "OrdenarAutor"),
        ("Ordenar por Ano de publicação", "OrdenarAno"),
        ("Sair", "Sair"),
    ]
    for i, (text, acao) in enumerate(botoes): # o for integare com a lista de botoes acima e com os comandos
        if acao == "Sair":
            btn = tk.Button(frame, text=text, command=root.destroy, width=20, bg="#ff6666", fg="white") #se a ação for "sair" ele cria um botão vermelho com a ação de sair da interface
        else:
            btn = tk.Button(frame, text=text, command=lambda a=acao: escolherOrdenacao(a), width=20, bg="#4CAF50", fg="white") #se não for a ação "sair" ele cria um botao que chama o comando

        btn.grid(row=i+1, column=0, pady=5)
def ordenarLivroPorTitulo():#lista por ordem alfabetica do titulo
    lista.ord_titulo()
    messagebox.showinfo("Ordenação", "A lista de livros foi ordenada por titulo.")

def ordenarLivroPorAutor():#ainda nao fiz
    lista.ord_autor()
    messagebox.showinfo("Ordenação", "A lista de livros foi ordenada por autor.")

def ordenarLivroPorAno():#ainda nao fiz
    lista.ord_ano()
    messagebox.showinfo("Ordenação", "A lista de livros foi ordenada por ano de publicação.")



#COMANDOS
def escolherAcao(acao):#função chamada na main para quando o usuario clicar, se o usuario clicar em adicionar, ele chamará o metodo adicionar acima

    if acao == "Adicionar":
     adicionarLivro()
    elif acao == "Buscar":
      buscarLivroPorTitulo()
    elif acao == "Exibir":
     listarLivros()
    elif acao == "Ordenar":
      ordenarLivros()

def escolherOrdenacao(acao):

    if acao == "OrdenarTitulo":
        ordenarLivroPorTitulo()
    elif acao == "OrdenarAutor":
        ordenarLivroPorAutor()
    elif acao == "OrdenarAno":
        ordenarLivroPorAno()

