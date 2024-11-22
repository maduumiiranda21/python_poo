from jogo import *

if __name__=='__main__':
    popo= Boxeador(" Popó ")
bambam = MMA ("Bambam")

print(popo)
print(bambam)

popo.cruzado(bambam)
print(bambam)
popo.gancho(bambam)
print(bambam)

bambam.superman_punch(popo)
print(popo)