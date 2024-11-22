from abc import ABC
class Atleta(ABC):
    nome: str
    idade: int
    peso: float
    
    def __init__(self, n:str, i: int, p:float):
        self.nome= n
        self.idade= i
        self.peso= p
        
    def aquecer(self):
        return '<<< Aquecendo !!! >>>\n'
    
    def __str__(self):
        info= f'Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso} kg\n'
        return info
    

class Corredor(Atleta):   
    def correr(self):
        return '<<< Correndo >>>\n'
    
class Nadador(Atleta):   
    def nadar(self):
        return '<<< Nadando >>>\n'
    
class Ciclista(Atleta):   
    def pedalar(self):
        return '<<< Pedalando >>>\n'
    
class Triatleta(Corredor,Nadador,Ciclista):
    def realizar_maratona(self):
        info= self.aquecer()
        info+= self.correr()
        info+= self.nadar()
        info+= self.pedalar()
        return info
        
        
    