public class livro {
    String autor;
    String titulo;
    Integer ano_publicacao;
  
    public livro(String autor, String titulo, Integer ano_publicacao){
      this.autor = autor;
      this.titulo = titulo;
      this.ano_publicacao = ano_publicacao;
    }
    public void verLivro() {
      System.out.println("Autor: " + autor + "\nTitulo: " + titulo + "\nAno de Publicação: " + ano_publicacao);
    }
    public void addLivro(){
      
    }

    public static void main(String[] args) {

  }
}


