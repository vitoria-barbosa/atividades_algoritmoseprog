def main():
    while True:

        falho, num = map(int, input().split())

        if falho == 0 and num == 0:
            break

        falho = str(falho)
        num = str(num)

        novo_numero = ""
        
        for n in num:
            if n == falho:
                continue
            else:
                novo_numero += n

        num_filtrado = filtrar_zeros(novo_numero)
        print(num_filtrado)


def filtrar_zeros(numero):
    numero = numero.lstrip('0')
    return numero if numero else '0'
    # se a string estiver vazia retorna 0
    

main()