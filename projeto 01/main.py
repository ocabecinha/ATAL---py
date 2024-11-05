import livro
import operacoes
import tkinter as tk


def main():
  
  lista = livro.metodos() # crio a variavel lista que vai receber os metodos adicionar, buscar, listar e ordenar
root = tk.Tk() #confesso que dei uma roubada no GPT pra fazer essa interface grafica, não ia perder meu tempo fazendo GUI
root.title("Gerenciador de Livros")
root.geometry("400x300")
root.configure(bg="#f5f5f5")

# Frame principal
frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(pady=20)

# Título
titulo_label = tk.Label(frame, text="Gerenciador de Livros", font=("Helvetica", 16, "bold"), bg="#f5f5f5")
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Botões de ação
botoes = [
  ("Adicionar Livro", "Adicionar"),#primeiro parametro é o texto do botão, e o segundo parametro é o comando de ação
  ("Buscar Livro", "Buscar"),
  ("Exibir Livros", "Exibir"),
  ("Ordenar Livros", "Ordenar"),
  ("Sair", "Sair"),
]

for i, (text, acao) in enumerate(botoes): # o for integare com a lista de botoes acima e com os comandos
  if acao == "Sair":
    btn = tk.Button(frame, text=text, command=root.quit, width=20, bg="#ff6666", fg="white") #se a ação for "sair" ele cria um botão vermelho com a ação de sair da interface
  else:
    btn = tk.Button(frame, text=text, command=lambda a=acao: operacoes.escolherAcao(a), width=20, bg="#4CAF50", fg="white") #se não for a ação "sair" ele cria um botao que chama o comando

  btn.grid(row=i+1, column=0, pady=5)

root.mainloop()

# Chamada principal
if __name__ == "__main__":
    main()