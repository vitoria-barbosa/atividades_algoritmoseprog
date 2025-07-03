# Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.
def main():
    maior = 0
    posicao = 0
    for i in range(1, 100+1):
        n = int(input())
        if n > maior:
            maior = n
            posicao = i

    print(maior)
    print(posicao)
            

main()