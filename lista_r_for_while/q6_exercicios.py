from utils import obter_num_int
def main():
    print("\n===== MONITORADOR DE PROGRESSO =====")
    qtd_sessoes = obter_num_int("Quantidade de sessões: ")
    soma_metade1 = 0
    soma_metade2 = 0
    metade = qtd_sessoes / 2
    maior_volume = 0

    for i in range(1, qtd_sessoes+1, 1):
        print(f"\nSessão {i}:")
        num_rep = obter_num_int("Número de repetições: ")
        peso = obter_num_int("Peso levantado: ")
        volume_total = num_rep * peso

        if i < metade:
            soma_metade1 += volume_total
        else:
            soma_metade2 += volume_total

        if volume_total > maior_volume:
            maior_volume = i

        print(f"\n-- Volume total da sessão: {volume_total}")

    situacao = classificar_progresso(soma_metade1, soma_metade2, metade)

    resultado = f"""
 ---------------------------------------------

 > Sessão com maior volume total: Sessão {maior_volume}
 > Situação: {situacao}
 """
    
    print(resultado)


def classificar_progresso(soma_metade1, soma_metade2, metade):
    media_metade1 = soma_metade1 / metade
    media_metade2 = soma_metade2 / metade
    return "Tendência de melhora observada" if media_metade2 > media_metade1 else "Não houve melhora significativa"


main()