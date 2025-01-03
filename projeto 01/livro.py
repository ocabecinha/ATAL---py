import tkinter as tk
from tkinter import simpledialog, messagebox

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.books = []  

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, author, book):
        node = self.root
        for char in author:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.books.append(book)

    def search(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.books
# # Vou destrinchar o código para explicar, fica melhor para estudarmos.
# Nessa primeira class estamos criando o obejto que vai ser passado na nossa lista encadeada que é uma pilha,
# ou seja, o "_init_" é o nosso construtor que vai passar todos os atributos pra dentro do objeto, coisa básica.
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.proximo = None
        # esse "self.proximo" é o nó da lista encadeada, ele nada mais é que o ponteiro indicando para o próximo livro que virá.
 
class metodos():
  def __init__(self):
    self.cabeca = None
    self.trie = Trie()
    # o "self.cabeca" quer indicar o primeiro livro, ou seja, outro ponteiro, só que apontando pro inicio.

  def adicionar_um_livro(self, titulo, autor, ano):
      novo_livro = Livro(titulo, autor, ano)  
      # cria um novo livro, e adiciona os atributos ao objeto.
      if not self.cabeca:
          self.cabeca = novo_livro
          self.trie.insert(autor, novo_livro)
          messagebox.showinfo("Sucesso", f"Livro '{titulo}' adicionado com sucesso.")
      else:
          atual = self.cabeca
          while atual.proximo:
              atual = atual.proximo
          atual.proximo = novo_livro
          messagebox.showinfo("Sucesso", f"Livro '{titulo}' adicionado com sucesso.")
            # se a lista não estiver vazia, ele primeiro percorre toda a lista, do primeiro até o ultimo e 
            # define o próximo do ultimo livro, como o novo livro, adicionando a lista.
        
  def listar_livros(self):
          livro_info = ""
          atual = self.cabeca
          while atual:
              livro_info += f"\nTítulo: {atual.titulo}, Autor: {atual.autor}, Ano: {atual.ano_publicacao}"
              atual = atual.proximo

          return livro_info
              # começa do primeiro livro e vai printando enquanto houver livros todos, movendo sempre para o proximo.
    

    #bubble sort

     #bubble sort          
  def ord_titulo(self):
      if not self.cabeca:
          return 
      # se a lista não tiver nada ele só retorna.
      troca = True
      # flag pra indicar troca de posições ou seja, se não houve trocas, a lista está ordenada.
      # /inicialização da váriavel troca.
      while troca:
          troca = False
          # definindo a troca como falsa até que se prove o contrario, o loop só continua enquanto troca for True.
          atual = self.cabeca
          while atual.proximo: 
              if atual.proximo.titulo.lower() < atual.titulo.lower():
                  # se o titulo do proximo livro for menor que o atual (ordem alfabética[eu te amo piton])
                  # troca de informações
                  atual.titulo, atual.proximo.titulo = atual.proximo.titulo, atual.titulo
                  atual.autor, atual.proximo.autor = atual.proximo.autor, atual.autor
                  atual.ano_publicacao, atual.proximo.ano_publicacao = atual.proximo.ano_publicacao, atual.ano_publicacao
                  troca = True
                  # definindo a troca como verdadeira para continuar o processo se necessário.
              atual = atual.proximo
      
    
      atual = self.cabeca
      while atual:
          print("\n" + atual.titulo)
          atual = atual.proximo
          # após toda a ordenação, um loop para printar todos os titulos.




  def ord_autor(self):
      if not self.cabeca:
          return

      troca = True

      while troca:
          troca = False

          atual = self.cabeca
          while atual.proximo:
              if atual.proximo.autor.lower() < atual.autor.lower():

                  atual.titulo, atual.proximo.titulo = atual.proximo.titulo, atual.titulo
                  atual.autor, atual.proximo.autor = atual.proximo.autor, atual.autor
                  atual.ano_publicacao, atual.proximo.ano_publicacao = atual.proximo.ano_publicacao, atual.ano_publicacao
                  troca = True

              atual = atual.proximo


      atual = self.cabeca
      while atual:
          print("\n" + atual.autor)
          atual = atual.proximo



  def ord_ano(self):
      if not self.cabeca:
          return

      troca = True

      while troca:
          troca = False

          atual = self.cabeca
          while atual.proximo:
              if atual.proximo.ano_publicacao > atual.ano_publicacao:

                  atual.titulo, atual.proximo.titulo = atual.proximo.titulo, atual.titulo
                  atual.autor, atual.proximo.autor = atual.proximo.autor, atual.autor
                  atual.ano_publicacao, atual.proximo.ano_publicacao = atual.proximo.ano_publicacao, atual.ano_publicacao
                  troca = True

              atual = atual.proximo


      atual = self.cabeca
      while atual:
          print("\n" + str(atual.ano_publicacao))
          atual = atual.proximo


  def buscarLivroPorAutor(self, autor):
    livros_sugeridos = self.trie.search(autor)
    atual = self.cabeca
    while atual:
        if atual.autor.lower() == autor.lower():  # Comparação insensível a maiúsculas
            for livro in livros_sugeridos:
                print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano: {livro.ano_publicacao}")
            return atual
        atual = atual.proximo
    return None

  

###########