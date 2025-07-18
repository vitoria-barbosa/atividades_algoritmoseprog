import funcoes_uteis as f
import utils as u

def main():
    menu = '''
 ================= ENEM POR ESCOLA - 2014 =================

  0 - Sair
  1 - Top N escolas do Brasil (todas as áreas)
  2 - Top N escolas do Brasil por área
  3 - Top N escolas por estado
  4 - Top N escolas por estado e rede
  5 - Média Nacional por área
  6 - Melhor escola por área do Brasil
  7 - Melhor escola por área do estado X
  8 - Melhor escola por área de todos os estados
  9 - Lista das escolas por estado ordenadas por renda
 10 - Busca escola específica por parte do nome
 11 - Ranking ENEM por estado
 12 - Ranking ENEM por região do país
  

 Sua opção >>>  '''
    
    u.limpar_tela()
    escolas = f.carregar_dados()
    opcao = u.obter_num_em_faixa(menu, 0, 12)

    while opcao != 0:

        if opcao == 1:
            u.limpar_tela()
            f.mostrar_n_top_escolas(escolas)

        elif opcao == 2:
            u.limpar_tela()
            f.mostrar_n_top_escolas_area(escolas)

        elif opcao == 3:
            u.limpar_tela()
            f.mostrar_n_top_escolas_estado(escolas)

        elif opcao == 4:
            u.limpar_tela()
            f.mostrar_n_top_escolas_estado_rede(escolas)

        elif opcao == 5:
            u.limpar_tela()
            f.mostrar_media_por_area(escolas)

        elif opcao == 6:
            u.limpar_tela()
            f.mostrar_melhor_escola_por_area(escolas)

        elif opcao == 7:
            u.limpar_tela()
            f.mostrar_melhor_escola_area_estado(escolas)

        elif opcao == 8:
            u.limpar_tela()
            f.mostrar_melhor_escola_area_todos_estados(escolas)

        elif opcao == 9:
            u.limpar_tela()
            f.mostrar_escolas_ordenadas_renda(escolas)

        elif opcao == 10:
            u.limpar_tela()
            f.buscar_escola_por_parte_nome(escolas)

        elif opcao == 11:
            u.limpar_tela()
            f.mostrar_ranking_por_estado(escolas)

        elif opcao == 12:
            u.limpar_tela()
            f.mostrar_ranking_por_regiao(escolas)

        u.enter_limpar_tela()
        opcao = u.obter_num_em_faixa(menu, 0, 12)


main()