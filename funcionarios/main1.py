from funcionarios import *

if __name__ == "__main__":
    G = Gerente("joao", "12345", 1234)
    print(G)
    if G.autenticar("1234", 1234):
        print(Gerente.cancelar_operacao())
    else:
        print("Falha na autenticacao")

    op = Operador_caixa("maria","54321", 4321, 1)
    print(op)
    if op.autenticar("1", 4321):
        print(op.registrar_produto())
    else:
        print("falha na autenticacao")

    seguranca = Segurança("jose","33333", 2323, 34)
    print(seguranca)
    if seguranca.autenticar("34", 2323):
        print(seguranca.acionar_alarme())
    else:
        print("Falha na autenticacao")
