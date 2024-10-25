class Frutas:
    def __init__(self):
        self.frutas = []

    # Adicionando uma fruta na pilha
    def empilhar(self, fruta):
        self.frutas.append(fruta)

    #eemovendo uma fruta da pilha
    def desempilhar(self):
        if len(self.frutas) == 0:
            print('A pilha está vazia'),
        else:
            return self.frutas.pop()

    #monstrado a fruta do topo sem remove-la
    def topo(self):
        if len(self.frutas) == 0:
            print('A pilha está vazia'),
        else:
            return self.frutas[-1]
  
    #numero de frutas na pilha
    def tamanho(self):
        return len(self.frutas)

    #todos as frutas da pilha
    def listar(self):
        return self.frutas

if __name__ == "__main__":
    frutas = Frutas()

    #empilhando as frutinhas
    frutas.empilhar("Maçã"),
    frutas.empilhar("Banana"),
    frutas.empilhar("Laranja"),

    print("Frutas na pilha:", frutas.listar()),
    
    #verificando o topo da pilha
    print("Topo da pilha:", frutas.topo()),

    #desempilhando uma fruta
    print("Desempilhando:", frutas.desempilhar()),
    
    print("Frutas na pilha após desempilhar:", frutas.listar()),
    
    #tamanho da pilha de frutas
    print("Tamanho da pilha:", frutas.tamanho())
    
    