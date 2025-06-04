# Supondo-se que a população de uma cidade A seja de 200.000 habitantes, com uma taxa anual de
# crescimento na ordem de 3.5%, e que a população de uma cidade B seja de 800.000 habitantes,
# crescendo a uma taxa anual de 1.35%, Escreva um algoritmo que determine quantos anos serão
# necessários, para que a população da cidade A ultrapasse a população da cidade B.
def main():
    pop_a = 200000
    pop_b = 800000
    anos = 0

    while not pop_a > pop_b:
        pop_a *= 1.035
        pop_b *= 1.0135
        anos += 1

    print(f"Serão necessários {anos} para que a população A ultrapasse a população B.")

main()