from utils import obter_num_float, obter_num_int
def main():
    print("\n====== SIMULADOR DE FINANCIAMENTO IMOBILIÁRIO ======")
    valor_imovel = obter_num_float("Valor do imóvel(R$): ")
    entrada = obter_num_float("Valor da entrada(R$): ")
    taxa = obter_num_float("Taxa de juros mensal(%): ")
    qtd_parcelas = obter_num_int("Quantidade de parcelas: ")
    capital = valor_imovel - entrada
    saldo_devedor = calcular_juros_compostos(capital, taxa, qtd_parcelas)
    parcela = saldo_devedor / qtd_parcelas
    print(saldo_devedor)
    print(f"A parcela ficará R$ {parcela:.2f}")

    for i in range(1, qtd_parcelas+1, 1):
        print(f"\nParcela {i}: ")
        saldo_devedor -= parcela
        print(f"Saldo devedor: {saldo_devedor:.2f}")

def calcular_juros_compostos(capital, taxa, qtd_parcelas):
    montante = capital * (1 + taxa / 100)** qtd_parcelas
    return montante

main()