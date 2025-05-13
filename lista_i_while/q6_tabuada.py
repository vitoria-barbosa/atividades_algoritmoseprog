# Escreva a tabuada dos números de 1 a 10.
def main():
    print(input('\nAperte >enter< para vizualizar a tabuada do 1 até o 10: '))
    print(calcular_tabuada(1))
    print(calcular_tabuada(2))
    print(calcular_tabuada(3))
    print(calcular_tabuada(4))
    print(calcular_tabuada(5))
    print(calcular_tabuada(6))
    print(calcular_tabuada(7))
    print(calcular_tabuada(8))
    print(calcular_tabuada(9))
    print(calcular_tabuada(10))

def calcular_tabuada(n: int):
    numero = 1
    while numero <= 10:
        multiplicacao = n * numero
        print(f'{n} X { numero} = {multiplicacao}')
        numero += 1
    return '---------------'

main()