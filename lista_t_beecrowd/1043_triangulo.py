# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
# Perimetro = XX.X
# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
# Area = XX.X
def main():
    entrada = input("")
    l1 = float(entrada.split()[0])
    l2 = float(entrada.split()[1])
    l3 = float(entrada.split()[2])
    if eh_triangulo(l1, l2, l3):
        perimetro = l1 + l2 + l3
        print(f"Perimetro = {perimetro:.1f}")
    else:
        area = (l1 + l2) * l3 / 2
        print(f"Area = {area:.1f}")


def eh_triangulo(l1, l2, l3):
    return l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2


main()