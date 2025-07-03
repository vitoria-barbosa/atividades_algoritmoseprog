def main():
    while True:
        regioes = int(input())

        if regioes == 0:
            break

        salto = 1
        while True:
             
            if ultima_regiao(regioes, salto) == 13:
                print(salto)
                break

            salto += 1


def ultima_regiao(regioes, saltos):
    regioes_restantes = list(range(1, regioes + 1))
                
    # Remove a Região 1 (que está no índice 0)
    regioes_restantes.pop(0) 
                
    # O índice atual para a contagem, após a primeira remoção.
    # Começa do início da lista reduzida.
    indice_atual = 0 

    # Continua removendo regiões até que reste apenas uma
    while len(regioes_restantes) > 1:
        # Calcula o índice da próxima região a ser removida
        indice_a_remover = (indice_atual + saltos - 1) % len(regioes_restantes)
                        
        # Remove a região nesse índice
        regioes_restantes.pop(indice_a_remover)
                        
        # Atualiza o índice para a próxima contagem
        # Se a remoção foi no último elemento, o próximo índice começa do 0.
        indice_atual = indice_a_remover % len(regioes_restantes)

    # A única região que sobrou é a última a ser desligada
    return regioes_restantes[0]

main()