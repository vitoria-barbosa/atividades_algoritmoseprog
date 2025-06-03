# Leia 2 (dois) números, calcule e escreva o mmc (mínimo múltiplo comum) entre os números lidos.
from utils import obter_num_int

def main():
    print("\n======== MMC ========")
    n1 = obter_num_int("Número 1: ")
    n2 = obter_num_int("Número 2: ")
    maior_num = n1 if n1 > n2 else n2
    mmc = calcular_mmc(maior_num, n1, n2)

    print(f"O MMC({n1},{n2}) = {mmc}")

def calcular_mmc(maior_num, n1, n2):
    
    for multiplo in range(maior_num, n1 * n2 + 1, maior_num):
        if multiplo % n1 == 0 and multiplo % n2 == 0:
            return multiplo
        
main()