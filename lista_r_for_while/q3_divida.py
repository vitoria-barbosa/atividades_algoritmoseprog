from utils import obter_num_int, obter_num_float
def main():
    print("\n====== QUITE SUA DÍVIDA ======")
    divida = obter_num_float("Valor da dívida: ")
    taxa = obter_num_float("Taxa de juros mensal(%): ")
    qtd_meses = obter_num_int("Quantidade de meses para projeção: ")
    saldo = divida

    for i in range(1, qtd_meses+1, 1):
        pagamento = obter_num_float(f"\nValor do pagamento do mês {i}: ")
        saldo = calcular_juros_compostos(saldo, taxa)
        saldo -= pagamento
        if saldo <= 0:
            print(f"\nA divida seria quitada no mês {i}.")
            return
        print(f"\nSaldo da dívida: R$ {saldo:.2f}")
        
    print(f"\nApós {qtd_meses} meses, a dívida ainda não seria quitada.")


def calcular_juros_compostos(capital, taxa):
    montante = capital * (1 + taxa / 100)** 1
    return montante
    
main()