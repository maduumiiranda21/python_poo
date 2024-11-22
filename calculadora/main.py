from calculadora import *

if __name__ == "__main__":
    calc = Calculadora()
    print(f'>>> {calc.resultado}')
    op = input('>>> ')

    while op != 'q':
        if op == '+' or op == '-' or op == '*' or op == '/':
            try:
                n = float(input('>>> '))
            except ValueError:
                print("Por favor, insira um número válido.")
                op = input('>>> ')
                continue

            if op == '+':
                o = Adicao(n)
            elif op == '-':
                o = Subtracao(n)
            elif op == '*':
                o = Multiplicacao(n)
            elif op == '/':
                o = Divisao(n)

            calc.add_operacao(o)
            
        elif op == '=':
            calc.calcular_total()
            print(f'>>> {calc.resultado}')
        elif op == 'd':
            calc.desfazer_ultima()
            print(f'>>> {calc.resultado}')

        op = input('>>> ')

