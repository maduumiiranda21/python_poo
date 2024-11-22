from abc import ABC

class Lutador(ABC):
    nome: str
    energia: float
    
    def __init__(self, n: str):
        self.nome= n
        self.energia= 100.0
    
    def soco(self,oponente):
        oponente.energia -= 5.5
        
    def __str__(self):
        info= f'Lutador: {self.nome}\nEnergia: {self.energia}\n'
        return info
  
class Boxeador(Lutador):
   #O parâmetro oponente é do tipo Lutador. Essa anotação : Lutador é uma dica de tipo para indicar que o argumento oponente deve ser uma instância da classe Lutador ou de uma classe semelhante.         
   
    def cruzado(self, oponente:Lutador):
        oponente.energia -= 10.2
        
    def gancho(self, oponente:Lutador):
        oponente.energia -= 20.8

class Muay_Thai(Boxeador):
    def chute_alto(self, oponente: Lutador):
        oponente.energia -= 15.4

class Jujitsu(Lutador):
    def chave_braco(self, oponente: Lutador):
        oponente.energia -= 100.0

class MMA(Muay_Thai, Jujitsu):
    def superman_punch(self, oponente: Lutador):
        oponente.energia -= 53.2
