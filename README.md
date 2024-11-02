# Gerenciador de Livros 📚

Este projeto é um sistema de gerenciamento de livros implementado em Python, que utiliza uma lista encadeada para armazenar e manipular informações sobre os livros. O sistema permite ao usuário adicionar livros, listar os livros armazenados e ordenar os livros por título ou autor. O sistema foi projetado para ser simples e intuitivo, permitindo que os usuários gerenciem suas coleções de livros de forma eficaz. A lista encadeada utilizada neste projeto permite adicionar e ordenar livros sem a necessidade de alocar uma quantidade fixa de espaço, tornando-o mais flexível e eficiente.

## Estrutura do Código 🗂️

Neste projeto, optamos por utilizar uma lista encadeada para armazenar os livros. A lista encadeada é uma estrutura de dados composta por nós, onde cada nó contém um valor e um ponteiro para o próximo nó. Essa estrutura oferece algumas vantagens em relação a arrays (ou listas dinâmicas)

## Algoritimo de Ordenação ⚙️

Para ordenar os livros, utilizamos o Bubble Sort, um algoritmo simples que compara elementos adjacentes e os troca de lugar se estiverem na ordem errada. Este processo é repetido até que não haja mais trocas a serem feitas, o que indica que a lista está ordenada.

## Funcionalidades ✅

1. **Adicionar livro**: O usuário pode adicionar um novo livro fornecendo o título, autor e ano de publicação.
2. **Listar livros**: Exibe todos os livros armazenados na lista.
3. **Ordenar livros por título**: Ordena a lista de livros em ordem alfabética com base nos títulos.
4. **Ordenar livros por autor**: Ordena a lista de livros em ordem alfabética com base nos autores.
5. **Ordernar livros por ano**: Ordena a lsita de livro em ordem de mais velho ao mais novo com base no ano de publicação.
6. **Pesquisar livro por titulo**: Pesquisa o livro pelo titulo buscado.
7. **Sair**: Encerra o programa.

### Classe Livro 📖

A classe `Livro` representa um livro e possui os seguintes atributos:

- `titulo`: O título do livro.
- `autor`: O autor do livro.
- `ano_publicacao`: O ano de publicação do livro.
- `proximo`: Um ponteiro para o próximo livro na lista encadeada.

### Exemplo de Uso 💻

Aqui estão alguns exemplos de como o sistema funciona:

```python

# Adicionar Livro
selecionar_opcao(1)  # Opção de adicionar livro
# 1° Exemplo
Digite o titulo = "Dom Casmurro"
Digite o nome autor = "Machado de Assis"
Digite o ano de publicação = 1899

# 2° Exemplo
Digite o titulo = "O Alquimista" 
Digite o nome autor = "Paulo Coelho"
Digite o ano de publicação = 1988

# Listar Livros
selecionar_opcao(2)  # Opção de listar livros
# Saída:
Título: Dom Casmurro, Autor: Machado de Assis, Ano: 1899
Título: O Alquimista, Autor: Paulo Coelho, Ano: 1988

# Ordenar Livros por Título
selecionar_opcao(3)  # Opção de ordenar livros por título
# Saída:
Título: Dom Casmurro, Autor: Machado de Assis, Ano: 1899
Título: O Alquimista, Autor: Paulo Coelho, Ano: 1988

# Ordenar Livros por Autor
selecionar_opcao(4)  # Opção para ordenar livros por autor
# Saída:
Título: Dom Casmurro, Autor: Machado de Assis, Ano: 1899
Título: O Alquimista, Autor: Paulo Coelho, Ano: 1988

# Exemplo de Sair
selecionar_opcao(5)  # Opção para sair
Saída: Saindo...
