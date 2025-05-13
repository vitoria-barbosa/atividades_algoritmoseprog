from package.io_utils import obter_numero_inteiro

def main():
    n = obter_n_maior_ou_igual_dois()
    somatorio = 0
    denominador = 1

    while denominador <= n:
        somatorio += (1 / denominador)
        denominador += 1

    print(f'Soma = {somatorio:.3f}')


def obter_n_maior_ou_igual_dois():
    n = obter_numero_inteiro('Digite um valor para N: ')
    if n >= 2:
        return n
    else:
        print('N deve ser maior ou igual a 2! Tente novamente: \n')
        return obter_n_maior_ou_igual_dois()

main()