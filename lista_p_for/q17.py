from utils import obter_num_inteiro

def main():
    n = obter_n_maior_ou_igual_dois()
    somatorio = 0

    for denominador in range(1, n+1, 1):
        somatorio += (1 / denominador)

    print(f'Soma = {somatorio:.3f}')


def obter_n_maior_ou_igual_dois():
    n = obter_num_inteiro('Digite um valor para N: ')
    if n >= 2:
        return n
    else:
        print('N deve ser maior ou igual a 2! Tente novamente: \n')
        return obter_n_maior_ou_igual_dois()

main()