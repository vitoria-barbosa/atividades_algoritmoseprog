from utils import obter_num_float, obter_num_int
def main():
    print("\n======== RETORNO DE INVESTIMENTO ========")
    qtd_imoveis = obter_num_int("Quantidade de imóveis a serem analisados: ")
    maior_retorno = 0
    maior_taxa_anualizada = 0

    for i in range(1, qtd_imoveis+1, 1):
        print(f"\nImóvel {i}: ")
        valor_compra = obter_num_float("Valor da compra: ")
        valor_aluguel = obter_num_float("Valor do aluguel mensal: ")
        qtd_anos = obter_num_int("Por quantos anos o imóvel esteve alugado: ")

        retorno_total = calcular_retorno_total(valor_compra, valor_aluguel, qtd_anos)
        taxa_retorno_anual = calcular_taxa_anualizada(retorno_total, qtd_anos)

        if retorno_total > maior_retorno:
            maior_retorno = i
            
        if taxa_retorno_anual > maior_taxa_anualizada:
            maior_taxa_anualizada = i
        
        print(f"\n> Retorno total: R$ {retorno_total:.2f}")
        print(f"> Taxa de retorno anualizada: {taxa_retorno_anual:.1f}%") 
    
    print(f"\n> Imóvel com maior retorno total: Imóvel {maior_retorno}")
    print(f"> Imóvel com maior taxa de retorno anualizada: Imóvel {maior_taxa_anualizada}")
    print("Fim.")


def calcular_retorno_total(valor_compra, aluguel, anos):
    return (aluguel * 12) * anos - valor_compra


def calcular_taxa_anualizada(retorno_total, anos):
    retorno_anual = retorno_total / anos
    taxa_percentual = (retorno_anual / retorno_total) * 100
    return taxa_percentual

main()