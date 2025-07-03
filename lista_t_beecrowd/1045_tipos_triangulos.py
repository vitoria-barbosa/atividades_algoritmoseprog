# Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:

# se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
# se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
# se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
# se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
# se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
# se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
def main():
    entrada = input("")
    a = float(entrada.split()[0])
    b = float(entrada.split()[1])
    c = float(entrada.split()[2])

    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a

    tipo_triangulo = classificar_triangulo(a, b, c)
    

def classificar_triangulo(a, b, c):
    if a >= b + c:
        print("NAO FORMA TRIANGULO")
    elif a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    elif a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    elif a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")
    

main()