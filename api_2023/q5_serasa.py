def main():
    # entrada
    print ("======== SCORE SERASA ========")
    criterio_a = obter_num_entre_um_e_cem("Critério A: ")
    criterio_b = obter_num_entre_um_e_cem("Critério B: ")
    criterio_c = obter_num_entre_um_e_cem("Critério C: ")
    # processamneto
    score1a = criterio_a / 100 * 260
    score1b = criterio_b / 100 * 570
    score1c = criterio_c / 100 * 170
    score2a = criterio_a / 100 * 620
    score2b = criterio_b / 100 * 190
    score2c = criterio_c / 100 * 190
    total_score1 = score1a + score1b + score1c
    total_score2 = score2a + score2b + score2c
    classificacao_score1 = classificar_score_antigo(total_score1)
    classificacao_score2 = classificar_score_novo(total_score2)
    # saída
    print(f"""
 ====== RESULTADO ======
 Score 1.0: {total_score1:.1f} - {classificacao_score1}
 Score 2.0: {total_score2:.1f} - {classificacao_score2}
 """)


def classificar_score_antigo(score):
    if score > 800:
        return 'Muito bom'
    elif score > 600:
        return 'Bom'
    elif score > 400:
        return 'Regular'
    else:
        return 'Baixo'
    

def classificar_score_novo(score):
    if score > 701:
        return 'Muito bom'
    elif score > 501:
        return 'Bom'
    elif score > 301:
        return 'Regular'
    else:
        return 'Baixo'


def obter_num_entre_um_e_cem(label):
    entrada = input(label)
    try:
        num = int(entrada)
        if num > 100 or num < 0:
            print('Digite um valor entre 0 e 100. Tente novamente: ')
            return obter_num_entre_um_e_cem(label)
        else:
            return num
    except ValueError:
        print('Digite um valor númerico! Tente novamente: ')
        return obter_num_entre_um_e_cem(label)

main()