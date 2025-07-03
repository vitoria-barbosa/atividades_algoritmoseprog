# Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.
def main():
    entrada = input("")
    a = int(entrada.split()[0])
    b = int(entrada.split()[1])
    c = int(entrada.split()[2])

    a2 = a
    b2 = b
    c2 = c

    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    
    print(a)
    print(b)
    print(c)
    print("")
    print(a2)
    print(b2)
    print(c2)


main()