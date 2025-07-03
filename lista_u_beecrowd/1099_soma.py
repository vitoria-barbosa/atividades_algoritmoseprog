# Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.
def main():
    n = int(input())

    for i in range(n):
        x, y = map(int, input().split())

        soma = 0
        if x > y:
            candidato = x - 1
            while candidato > y:
                if not candidato % 2 == 0:
                    soma += candidato

                candidato -= 1
        
            print(soma)
        else:
            candidato = x + 1
            while candidato < y:
                if not candidato % 2 == 0:
                    soma += candidato

                candidato += 1
        
            print(soma)

main()