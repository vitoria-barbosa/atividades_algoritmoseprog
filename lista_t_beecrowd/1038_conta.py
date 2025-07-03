def main():
    entrada = input("")
    codigo = (entrada.split()[0])
    qtd = int(entrada.split()[1])
    comidas = {"1": 4, "2": 4.50, "3": 5, "4": 2, "5": 1.50}
    valor = comidas[codigo]
    total = qtd * valor

    print(f"Total: R$ {total:.2f}")

main()