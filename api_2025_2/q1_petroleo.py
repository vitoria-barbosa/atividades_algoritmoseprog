import utils as u

def main():
    qtd_bombas = u.obter_num_int("Quantidade de bombas: ")
    valor_inicial_barris = u.obter_num_int("Valor inicial de barris por bomba: ")
    taxa_reducao = u.obter_num_float("Taxa de redução de barris(%): ")
    limite_min = u.obter_num_int("Limite mínimo de barris permitido por bomba: ")
    ciclos = 0
    qtd_barris = valor_inicial_barris
    somatorio_barris = 0

    while qtd_barris > limite_min:
        ciclos += 1
        diminuicao = (taxa_reducao/100) * qtd_barris
        qtd_barris -= diminuicao
        somatorio_barris += qtd_barris

    qtd_ciclos_total = ciclos * qtd_bombas
    barris_extraidos = somatorio_barris * qtd_bombas

    print(f"\nCiclos realizados por bomba: {ciclos}")
    print(f"Quantidade de ciclos total para {qtd_bombas} bombas: {qtd_ciclos_total}")
    print(f"Quantidade de barris extraidos em {qtd_bombas} bombas: {barris_extraidos:.0f}")


main()