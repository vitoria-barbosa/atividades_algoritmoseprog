# Escreva um algoritmo para determinar o número de dígitos de um número informado.
def main():
    qtd_digitos = obter_numero_e_qtd()

    print(f"\nSeu número tem {qtd_digitos} dígitos.")

def obter_numero_e_qtd():
    entrada = input("Digite um número: ")

    try:
        eh_num = int(entrada)
        qtd_digitos = len(entrada)
        return qtd_digitos
    
    except ValueError:
        print("entrada inválida. Digite um valor inteiro e numérico.")
        return obter_numero_e_qtd()

main()