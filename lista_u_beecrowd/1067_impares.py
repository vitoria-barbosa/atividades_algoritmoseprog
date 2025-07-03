# Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.
def main():
    n = int(input())
    candidato = 1
    while candidato <= n:
        if not candidato % 2 == 0:
            print(candidato)
        
        candidato += 1

main()