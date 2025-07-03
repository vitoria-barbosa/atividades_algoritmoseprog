# Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.
def main():
    positivos = 0
    soma = 0
    for i in range(6):
        n = float(input(""))
        if n > 0:
            positivos += 1
            soma += n
    
    media = soma / positivos

    print(f"{positivos} valores positivos")
    print(f"{media:.1f}")

main()