from atletas import *

if __name__=='__main__':
    c1 = Corredor(" Bolt zayn", 35, 90.6)
    n1 = Nadador(" Henrique", 20, 65.0)
    ciclista1 = Ciclista("Joao", 19, 103.0)
    tri = Triatleta(" Fernandinha", 42, 65.3)

    print(c1)
    print(c1.aquecer())
    print(c1.correr())

    print(n1)
    print(n1.aquecer())
    print(n1.nadar())

    print(ciclista1)
    print(ciclista1.aquecer())
    print(ciclista1.pedalar())

    print(tri)
    print(tri.realizar_maratona())

    print(Triatleta.__mro__)
    
   