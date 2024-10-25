import livro
    
def main():
  
  lista = livro.ListadeLivros()
  
  while True:
    print("\n1 Adicionar livro")
    print("2 Listar livros")
    print("3 Ordernar livros por titulo")
    print("4 Sair")
    r = input("Selecione oque você quer: ")
    
    if r == '1':
      titulo = input("Digite o titulo do livro: ")
      autor = input("Digite o nome do autor: ")
      ano = int(input("Digite o ano de publicação: "))
      lista.adicionar_um_livro(titulo, autor, ano)
      
    elif r == '2':
      lista.listar_livros()
      
    elif r == '3':
      lista.sort_titulo()
      print('Livros ordenados por titulo')
      
    elif r == '4':
      print('Saindo')
      break
    
    else: 
      return 'Opção inválida'