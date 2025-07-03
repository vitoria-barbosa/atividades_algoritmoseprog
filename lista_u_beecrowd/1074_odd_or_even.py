# Leia um valor inteiro N. Este valor será a quantidade de valores que serão lidos em seguida. Para cada valor lido, mostre uma mensagem em inglês dizendo se este valor lido é par (EVEN), ímpar (ODD), positivo (POSITIVE) ou negativo (NEGATIVE). No caso do valor ser igual a zero (0), embora a descrição correta seja (EVEN NULL), pois por definição zero é par, seu programa deverá imprimir apenas NULL.
def main():
    n = int(input())

    for i in range(n):
        x = int(input())
        if x == 0:
            print("NULL")
        elif x % 2 == 0:
            print("EVEN", end=" ")
            if x > 0:
                print("POSITIVE")
            elif x < 0:
                print("NEGATIVE")
        else:
            print("ODD", end=" ")
            if x > 0:
                print("POSITIVE")
            elif x < 0:
                print("NEGATIVE")

main()