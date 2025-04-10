def principal():
    a = int(input('Digite um número inteiro e positivo: '))
    b = int(input('Digite outro número inteiro e positivo: '))
    c = int(input('Digite mais um número inteiro e positivo: '))
    r = (a + b) ** 2
    s = (b + c) ** 2
    resultado = (r + s) / 2

    print(f'\nResultado da expressão ({a}+{b})² + ({b}+{c})² /2 = {resultado:.1f}')

principal()
