class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.proximo = None

class ListadeLivros: 
  def __init__(self):
    self.cabeca = None
    
  def adicionar_um_livro(self, titulo, autor, ano):
      novo_livro = Livro(titulo, autor, ano)  
      if not self.cabeca:
          self.cabeca = novo_livro
      else:
          atual = self.cabeca
          while atual.proximo:
              atual = atual.proximo
          atual.proximo = novo_livro  

        
  def listar_livros(self):
          atual = self.cabeca
          while atual:
              print(f"Título: {atual.titulo}, Autor: {atual.autor}, Ano: {atual.ano_publicacao}"),
              atual = atual.proximo
    
  #bubble sort           
  def sort_titulo(self):
    if not self.cabeca:
      return
    troca = True
    
    while troca:
      troca = False, 
      atual = self.cabeca
      while atual.proximo: 
        if atual.proximo > atual.proximo.titulo:
          #troca de info.
          atual.titulo, atual.proximo.titulo = atual.proximo.titulo, atual.proximo
          atual.autor, atual.proximo.autor = atual.proximo.autor, atual.autor
          atual.ano_publicacao, atual.proximo.ano_publicacao = atual.proximo.ano_publicacao, atual.ano_publicacao
          troca = True
        atual = atual.proximo
      