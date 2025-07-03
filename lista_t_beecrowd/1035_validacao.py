# Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos"
def main():
    entrada = input("")
    a = int(entrada.split()[0])
    b = int(entrada.split()[1])
    c = int(entrada.split()[2])
    d = int(entrada.split()[3])

    print(validar_valores(a, b, c, d))
    
def validar_valores(a, b, c, d):
    return "Valores aceitos" if b > c and d > a and (c + d) > (a + b) and c >= 0 and d >= 0 and eh_par(a) else "Valores nao aceitos"


def eh_par(n):
    return n % 2 == 0


main()