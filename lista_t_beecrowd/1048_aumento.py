def main():
    salario = float(input(""))

    if 0 <= salario <= 400:
        percentual = 15
        aumento = 15/100 * salario
    elif 400 < salario <= 800:
        percentual = 12
        aumento = 15/100 * salario
    elif 800 < salario <= 1200:
        percentual = 10
        aumento = 10/100 * salario
    elif 1200 < salario <= 2000:
        percentual = 7
        aumento = 7/100 * salario
    else:
        percentual = 4
        aumento = 4/100 * salario
    
    novo_salario = salario + aumento
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {aumento:.2f}")
    print(f"Em percentual: {percentual} %")

main()