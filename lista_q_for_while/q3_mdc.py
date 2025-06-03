from utils import obter_num_int

def main():
    print("\n======== MDC ========")
    n1 = obter_num_int("Número 1: ")
    n2 = obter_num_int("Número 2: ")
    menor = n1 if n1 < n2 else n2
    mdc = calcular_mdc(menor, n1, n2)

    print(f"\nO MDC({n1},{n2}) = {mdc}")


def calcular_mdc(menor, n1, n2):

    for divisor in range(menor, 0, -1):
        if n1 % divisor == 0 and n2 % divisor == 0:
            return divisor
        
main()