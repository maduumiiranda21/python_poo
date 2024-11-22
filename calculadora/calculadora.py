from abc import ABC, abstractmethod
from typing import List

class Operação(ABC):
    operador: float
    
    def __init__(self, n: float):
        self.operador= n
        
    @abstractmethod
    def calcular(self, n:float):
        pass
    
    @abstractmethod
    def calcular_inverso(self, n: float):
        pass
    
class Divisao(Operação):
    def calcular(self, n: float):
        return n / self.operador
    
    def calcular_inverso(self, n: float):
        return n * self.operador
        
class Multiplicacao(Operação):
    def calcular(self, n: float):
        return n * self.operador
    
    def calcular_inverso(self, n: float):
        return n / self.operador

class Adicao(Operação):
    def calcular(self, n: float):
        return n + self.operador
    
    def calcular_inverso(self, n: float):
        return n - self.operador
    
class Subtracao(Operação):
    def calcular(self, n: float):
        return n - self.operador
    
    def calcular_inverso(self, n: float):
        return n + self.operador
    
class Calculadora:
    resultado: float
    operacoes: List[Operação]
    
    def __init__(self):
        self.resultado= 0
        self.operacoes = []
        
    def add_operacao(self, op: Operação):
        self.operacoes.append(op)
        
    def calcular_total(self):
        calculo = 0
        for op in self.operacoes:
            calculo = op.calcular(calculo)  
        self.resultado = calculo
    
    def desfazer_ultima(self):
        op = self.operacoes.pop(op)
        self.resultado = op.calcular_inverso(self.resultado)
        
   
        
        
        

