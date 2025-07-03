def main():
    n = int(input())

    total = 0
    coelhos = 0
    ratos = 0
    sapos = 0

    for i in range(n):
        entrada = input()
        qtd = int(entrada.split()[0])
        animal = entrada.split()[1]
        total += qtd

        if animal == "C":
            coelhos += qtd
        elif animal == "R":
            ratos += qtd
        else:
            sapos += qtd
    
    print(f"Total: {total} cobais")
    print(f"Total de coelhos: {coelhos}")
    print(f"Total de ratos: {ratos}")
    print(f"Total de sapos: {sapos}")
    print(f"Percentual de coelhos: {coelhos/total * 100:.2f} %")
    print(f"Percentual de ratos: {ratos/total * 100:.2f} %")
    print(f"Percentual de sapos: {sapos/total * 100:.2f} %")

main()
