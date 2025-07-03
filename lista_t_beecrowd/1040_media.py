# Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela mensagem "Media: ". Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas, o programa deve imprimir a mensagem "Aluno em exame.".
# No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno. Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais ) ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.
def main():
    entrada = input("")
    n1 = float(entrada.split()[0])
    n2 = float(entrada.split()[1])
    n3 = float(entrada.split()[2])
    n4 = float(entrada.split()[3])

    media = media_ponderada(n1, n2, n3, n4)
    print(f"Media: {media:.1f}")
    situacao = classificar_media(media)
    print(situacao)

    if situacao == "Aluno em exame.":
        nota = float(input(""))
        print(f"Nota do exame: {nota:.1f}")
        nova_media = (media + nota) / 2
        nova_situacao = "Aluno aprovado." if nova_media >= 5 else "Aluno reprovado."
        print(nova_situacao)
        print(f"Media final: {nova_media:.1f}")


def classificar_media(media):
    if media < 5:
        return "Aluno reprovado."
    elif 5 <= media < 7:
        return "Aluno em exame."
    else:
        return "Aluno aprovado." 


def media_ponderada(n1, n2, n3, n4):
    return (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10


main()