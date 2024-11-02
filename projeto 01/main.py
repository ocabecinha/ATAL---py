import livro
    
def main():
  
  lista = livro.ListadeLivros()
  
  while True:
    print("\n1 Adicionar livro")
    print("2 Listar livros")
    print("3 Ordernar livros por titulo")
    print("4 Ordernar livros por autor")
    print("5 Ordernar livros por ano de publicação")
    print("6 Buscar livro por titulo")
    print("7 Sair")
    r = input("\nSelecione oque você quer: ")
    
    if r == '1':
      titulo = input("Digite o titulo do livro: ")
      autor = input("Digite o nome do autor: ")
      ano = int(input("Digite o ano de publicação: "))
      lista.adicionar_um_livro(titulo, autor, ano)
      
    elif r == '2':
      lista.listar_livros()
      
    elif r == '3':
      print('Livros ordenados por titulo')
      lista.ord_titulo()
    
    elif r == '4':
      print('Livros ordenados por autor')
      lista.ord_autor()

    elif r == '5':
      print('Livros ordenados por ano de publicação')
      lista.ord_ano()

  
    elif r =='6':
      titulo = input("Digite o titulo do livro que você quer encontrar: ")
      lista.buscar_por_titulo(titulo)
    
    elif r =='7':
      print('Saindo...')
      break
    
    else: 
      return 'Opção inválida'

# Chamada principal
if __name__ == "__main__":
    main()