import utils as u

def main():
    qtd_provas = u.obter_num_em_faixa("Quantas provas você fez: ", 2, 6)
    somatorio_notas = 0
    somatorio_pesos = 0
    somatorio_notas_com_pesos = 0

    for i in range(qtd_provas):
        nota = u.obter_num_float(f"Nota da prova {i+1}: ")
        peso = u.obter_num_em_faixa(f"Peso da nota {i+1} (1 a 3): ", 1, 3)

        somatorio_notas_com_pesos += nota * peso
        somatorio_notas += nota
        somatorio_pesos += peso

    media_ponderada = somatorio_notas_com_pesos / somatorio_pesos
    media = somatorio_notas / qtd_provas

    print(f"\nSua nota ponderada foi: {media_ponderada:.1f}")
    print(f"\nSua média seria {media} se não houvesse pesos.")
    
    if media_ponderada >= 8:
        print("\nSua nota foi maior ou igual a oito, você está de parabéns!!!")


main()