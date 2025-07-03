# Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.
def main():
    nota1 = validar_nota()
    nota2 = validar_nota()

    media = (nota1 + nota2) / 2
    print(f"media = {media:.2f}")


def validar_nota():
    nota = float(input())

    if nota < 0 or nota > 10:
        print("nota invalida")
        return validar_nota()
    else:
        return nota

main()