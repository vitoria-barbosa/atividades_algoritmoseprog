def main():
    salario = float(input(""))

    if salario <= 2000:
        print("Isento")

    elif salario <= 3000:
        saldo = salario - 2000
        imposto =  8/100 * saldo
        print(f"R$ {imposto:.2f}")
    elif salario <= 4500:
        saldo1 = salario - 2000
        taxa1 = 8/100 * 1000
        saldo2 = saldo1 - 1000
        taxa2 = 18/100 * saldo2
        imposto = taxa1 + taxa2
        print(f"R$ {imposto:.2f}")
    else:
        saldo1 = salario - 2000
        taxa1 = 8/100 * 1000
        saldo2 = saldo1 - 1000
        taxa2 = 18/100 * 1500
        saldo3 = saldo2 - 1500
        taxa3 = 28/100 * saldo3
        imposto = taxa1 + taxa2 + taxa3
        print(f"R$ {imposto:.2f}")


main()