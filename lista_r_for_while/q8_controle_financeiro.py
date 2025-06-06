from utils import obter_num_int, obter_num_float
def main():
    print("\n======== CONTROLE FINANCEIRO ========")
    soma_receitas = 0
    maior_receita = 0
    id_maior_receita = " "
    soma_despesas = 0
    maior_despesa = 0
    id_maior_despesa = " "

    qtd_receitas = obter_num_int("\nQuantas receitas quer registrar: ")

    for i in range(1, qtd_receitas+1, 1):
        print(f"\nReceita {i}: ")
        descricao = input("Descrição: ")
        valor = obter_num_float("Valor(R$): ")

        soma_receitas += valor

        if valor > maior_receita:
            maior_receita = valor
            id_maior_receita += descricao

    qtd_despesas = obter_num_int("\nQuantas despesas quer registrar: ")

    for i in range(1, qtd_despesas+1, 1):
        print(f"\nDespesa {i}: ")
        descricao = input("Descrição: ")
        valor = obter_num_float("Valor(R$): ")

        soma_despesas += valor

        if valor > maior_despesa:
            maior_despesa = valor
            id_maior_despesa += descricao

    saldo = soma_receitas - soma_despesas

    resultado = f"""
 -----------------------------------------------------
 Total de receitas: R$ {soma_receitas:.2f} 
 Total de despesas: R$ {soma_despesas:.2f} 
 Saldo final do mês: R$ {saldo:.2f}
 Maior receita: {id_maior_receita}\tValor: R$ {maior_receita:.2f}
 Maior despesa: {id_maior_despesa}\tValor: R$ {maior_despesa:.2f}
 """
    
    print(resultado)

main()