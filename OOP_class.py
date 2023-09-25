
class Elevador:
    def __init__(self, totalCapacidade, atualCapacidade, totalAndar, atualAndar):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = atualCapacidade
        self.totalAndar = totalAndar
        self.atualAndar = atualAndar
        
    def subir(self):
        if self.atualAndar < self.totalAndar:
            self.atualAndar += 1
            print ("Subindo...")
        else:
            print("Você já está no andar mais alto")

    def descer(self):
        if self.atualAndar > 0:
            self.atualAndar -= 1
            print ("Descendo...")
        else:
            print("Você está no terreo")

    def entrar(self):
        if self.atualCapacidade < self.totalCapacidade:
            self.atualCapacidade += 1
            print ("Entrando...")
        else:
            print("O elevador está cheio")

    def sair(self):
        if self.atualCapacidade >= 1:
            self.atualCapacidade -= 1
            print ("Saindo...")
        else:
            print("Não tem ninguem")



    
    
