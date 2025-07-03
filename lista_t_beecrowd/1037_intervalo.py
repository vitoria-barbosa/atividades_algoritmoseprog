# Você deve fazer um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Obviamente se o valor não estiver em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.
def main():
    valor = float(input(""))

    if 0 <= valor <= 25:
        print("Intervalo [0,25]")
    elif 25 < valor <= 50:
        print("Intervalo (25,50]")
    elif 50 < valor <= 75:
        print("Intervalo (59,75]")
    elif 75 < valor <= 100:
        print("Intervalo (75,100]")
    else:
        print("Fora do intervalo")

main()