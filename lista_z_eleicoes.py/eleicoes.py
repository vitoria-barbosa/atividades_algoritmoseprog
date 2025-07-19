import funcoes_uteis as f

def main():
    print("\n>>>>> ELEIÇÕES TERESINA 2012 <<<<<\n")

    coligacoes = f.carregar_partidos()
    candidatos = f.carregar_candidatos()

    votos_total = f.somar_votos(candidatos)
    print(f"- Total de votos válidos: {votos_total}")
    print("- Quantidade de vagas para vereadores: 29")
    quociente_eleitoral = f.calcular_quociente_eleitoral(votos_total, 29)
    print(f"- Quociente eleitoral: {quociente_eleitoral}")

    coligacoes = f.computar_total_votos_por_coligacao(coligacoes, candidatos)
    coligacoes = sorted(coligacoes, key= lambda x: x['total_votos'], reverse=True)

    print(f"\n- Total de votos por partido/coligação:\n")

    for coligacao in coligacoes:
        print(f"{coligacao['coligacao']} - Votos: {coligacao.get('total_votos')}")


    coligacoes = f.calcular_quociente_partidario(coligacoes, quociente_eleitoral)

    print(f"\n- Total de vagas por partido/coligação:\n")
    soma_vagas = 0

    for coligacao in coligacoes:
        print(f"{coligacao['coligacao']} - Vagas: {coligacao['qtd_vagas']}")
        soma_vagas += coligacao.get('qtd_vagas')

    vagas_restantes = 29 - soma_vagas
    print(f"\nVagas distribuídas: {soma_vagas}")
    print(f"Vagas restantes: {vagas_restantes}")

    coligacoes = f.distribuir_vagas_restantes(coligacoes, vagas_restantes)
    print(f"\n- Novo total de vagas por partido/coligação:\n")

    for coligacao in coligacoes:
        print(f"{coligacao['coligacao']} - Vagas: {coligacao['qtd_vagas']}")


main()