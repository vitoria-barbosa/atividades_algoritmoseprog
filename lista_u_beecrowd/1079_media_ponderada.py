# Leia 1 valor inteiro N, que representa o número de casos de teste que vem a seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o terceiro valor tem peso 5.
def main():
    n = int(input())

    for i in range(n):
        n1, n2, n3 = map(float, input().split())

        media_ponderada = (n1*2 + n2*3 + n3*5) / 10

        print(f"{media_ponderada:.1f}")

        
main()