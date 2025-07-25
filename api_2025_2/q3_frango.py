import utils as u

def main():
        qtd_max = u.obter_num_int("Quantidade máxima de caixas: ")
        peso_max = u.obter_num_float("Peso máximo(toneladas): ")
        peso_max_kg = peso_max * 1000
        qtd_caixas = 0
        peso_acumulado = 0

        while qtd_caixas < qtd_max:
        
            peso = u.obter_num_float("Peso da caixa(kg): ")
            peso_acumulado += peso

            if peso == 0:
                break

            qtd_caixas += 1   

            if peso_acumulado > peso_max_kg:
                peso_acumulado -= peso
                qtd_caixas -= 1
                break


        print(f"\nQuantidade de caixas: {qtd_caixas}")
        print(f"Peso total da carga: {peso_acumulado:.1f} kg")


main()