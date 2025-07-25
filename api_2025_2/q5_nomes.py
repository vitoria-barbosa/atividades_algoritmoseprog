def main():
    qtd_nomes = 0
    nome = input("Nome: ")

    while nome != 'fim':

        nome = remover_espacos(nome)

        if len(nome) >= 4:
            qtd_nomes += 1

        nome = input("Nome: ")

    print(f"\nForam digitados {qtd_nomes} nome(s).")


def remover_espacos(nome):
    novo_nome = ""
    for caractere in nome:
        if caractere != ' ':
            novo_nome += caractere

    return novo_nome

main()