# eia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.
def main():
    entrada = input("")
    a = int(entrada.split()[0])
    b = int(entrada.split()[1])

    maior = a if a > b else b
    menor = a if a < b else b
    if maior % menor == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao multiplos")

        
main()