# Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente do algarismo da unidade.

def main():
    num = obter_numero_inteiro_dois_digitos('Digite um número de 2 dígitos: ')

    eh_igual(num)


def eh_igual(num):
    d = num // 10
    u = num % 10
    if d == u:
        print(f'\nA dezena e a unidade do número {num} são iguais.')
    else:
        print(f'\nA dezena e a unidade do número {num} são diferentes.')


def obter_numero_inteiro_dois_digitos(label: str):
    numero = int(input(label))
    if numero / 10 >= 1 and numero / 10 < 10:
        return numero
    else:
        print('\nO número deve ter dois dígitos.\n')
        return obter_numero_inteiro_dois_digitos(label)


main()