from utils import obter_n_maior_ou_igual_dois

def main():
    n = obter_n_maior_ou_igual_dois()
    somatorio = 0
    numerador = 1

    for denominador in range(n, 0, -1):
        somatorio += (numerador / denominador)
        numerador += 1

    print(f'Soma das frações = {somatorio:.3f}')

main()