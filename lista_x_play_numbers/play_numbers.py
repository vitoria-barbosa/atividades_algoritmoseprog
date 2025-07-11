import utils as u
import vetor_utils as v_u

def main():
    
    
    
    u.limpar_tela()
    vetor = v_u.inicializar_vetor()
    
    opcao = u.obter_num_em_faixa(u.mostar_menu(), 0, 14)
    
    while opcao != 0:

        if opcao == 1:
            print()
            print(vetor)

        elif opcao == 2:
            v_u.resetar_vetor(vetor)

        elif opcao == 3:
            print(f"\nNo vetor há {len(vetor)} itens.")

        elif opcao == 4:
            v_u.maior_valor_e_posicao(vetor)
            v_u.menor_valor_e_posicao(vetor)

        elif opcao == 5:
            somatorio = v_u.calcular_somatorio(vetor)
            print(f"\nSomatório dos itens: {somatorio}")

        elif opcao == 6:
            media = v_u.calcular_media(vetor)
            print(f"\nA média de todos os itens é: {media:.2f}")

        elif opcao == 7:
            lista_filtrada = v_u.filtrar(vetor, lambda x:x>0)
            print(f"\nHá {len(lista_filtrada)} itens positivos. São eles:\n")
            print(lista_filtrada)

        elif opcao == 8:
            lista_filtrada2 = v_u.filtrar(vetor, lambda x:x<0)
            print(f"\nHá {len(lista_filtrada2)} itens negativos. São eles:\n")
            print(lista_filtrada2)


        elif opcao == 9:
            escolha = u.obter_num_em_faixa(u.mostrar_menu2(), 1, 6)
            
            if escolha == 1:
                valor = float(input("\nDigite o valor que quer multiplicar: "))
                vetor = v_u.mapear(vetor, lambda x:x*valor)
                print("\nVetor atualizado com sucesso!")

            elif escolha == 2:
                expoente = u.obter_num_positivo("\nExpoente que quer elevar: ")
                vetor = v_u.mapear(vetor, lambda x:x**expoente)
                print("\nVetor atualizado com sucesso!")
                
            elif escolha == 3:
                numerador, denominador = map(int, input("\nFração (Ex: x/y): ").split('/'))
                vetor = v_u.mapear(vetor, lambda item:item * (numerador/denominador))
                print("\nVetor atualizado!")
                
            elif escolha == 4:
                min, max = map(int, input("\nMínimo e máximo: ").split())
                v_u.substituir_valores_negativos(vetor, min, max)
                print("\nVetor atualizado com sucesso!")

            elif escolha == 5:
                ordem = input("\nDe forma crescente ou decrescente? (C/D): ")

                if ordem.upper() == 'C':
                    vetor.sort()

                elif ordem.upper() == 'D':
                    vetor.sort(reverse=True)
                
                print("\nVetor ordenado com sucesso!")
            
            elif escolha == 6:
                vetor = v_u.embaralhar(vetor)
                print("\nVetor embaralhado com sucesso!")
            
        elif opcao == 10:
            qtd_valores = u.obter_num_positivo("\nQuantos valores quer adicionar: ")

            for _ in range(qtd_valores):
                novo_valor = u.obter_numero("Novo número: ")
                vetor.append(novo_valor)
            
            print("Valor(es) adicionado(s) com sucesso!")
        
        elif opcao == 11:
            print(f"\nVetor: {vetor}")
            n = u.obter_numero("Valor que quer remover: ")
            vetor = v_u.filtrar(vetor, lambda x:x!=n)
            print("\nValores removidos com sucesso!")
        
        elif opcao == 12:
            print(f"\nVetor: {vetor}")
            posicao_remover = u.obter_numero("Posição que quer remover: ")
            vetor = v_u.remover_por_posicao(vetor, posicao_remover)
            print("\nValor removido com sucesso!")
        
        elif opcao == 13:
            print(f"\nVetor: {vetor}")
            posicao_editar = u.obter_numero("Posição que quer editar: ")
            valor_novo = u.obter_numero("Novo número: ")
            vetor = v_u.editar_por_posicao(vetor, posicao_editar, valor_novo)
            print("\nValor editado com sucesso!")

        elif opcao == 14:
            v_u.salvar_em_arquivo(vetor)
            print("Operação realizada com sucesso!")
    
        u.limpar_tela()        
        opcao = u.obter_num_em_faixa(u.mostar_menu(), 0, 14)
    

main()