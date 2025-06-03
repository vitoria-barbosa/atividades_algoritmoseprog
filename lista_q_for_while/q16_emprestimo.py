# Uma companhia financeira debita um juro de 0.85% diário sobre o saldo não pago de um empréstimo.
# Com um empréstimo de R$ 3.000,00, um pagamento de R$ 200,00 é feito todo dia útil. Escreva um
# algoritmo que calcule quantos dias úteis são necessários para se concluir o pagamento do empréstimo.
def main():
    dias = 0
    emprestimo = 3000

    while emprestimo > 0:
        juros = 0.0085 * emprestimo
        emprestimo += juros
        emprestimo -= 200
        dias += 1

    print(f"\nO empréstimo de 3.000 será quitado em {dias} dias úteis.")


main()