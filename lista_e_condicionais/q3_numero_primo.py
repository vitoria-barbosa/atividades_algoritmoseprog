import sys
sys.path.append('C:\\Users\\vitor\\algoritmos_e_prog\\lista_f_condicionais')

from package.io_utils import obter_numero_inteiro

def main():
    print('\n------É primo?------')
    num = obter_numero_inteiro('Digite um número: ')
    print(eh_primo(num))


def eh_primo(n: int):
    if n <= 1:
        return f'{n} não é primo'
    elif n == 2 or n == 3:
        return f'{n} é primo'
    elif n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
        return f'{n} é primo'
    else:
        return f'{n} não é primo'


main()    