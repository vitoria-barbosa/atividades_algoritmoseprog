# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.
import math
def main():
    entrada = input("")
    a = float(entrada.split()[0])
    b = float(entrada.split()[1])
    c = float(entrada.split()[2])
    delta = calcular_delta(a, b, c)

    if delta < 0 or a == 0:
        print("Impossivel calcular")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        print(f"R1 = {x1:.5f}")
        print(f"R2 = {x2:.5f}")


def calcular_delta(a, b, c):
    return b**2 - 4 * a * c
    

main()