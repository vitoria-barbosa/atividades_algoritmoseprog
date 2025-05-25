# Dado um número inteiro N, e N sequências de
# números inteiros terminadas por 0, calcular e imprimir:
# a. A soma dos números pares de cada sequência.
# b. A média de todos os números digitados de todas as
# sequências.
# c. O menor e o maior números digitados de todas as sequências.
# começo 12:30 fim : 13:30
import os
from q1_number_utils import obter_numero_int_positivo
def main():
    qtd = obter_numero_int_positivo("Digite a quantidade de sequências: ")
    contador = qtd

    while contador > 0:
        print("Digite uma sequência de números, o último sendo 0.\n")
        maior_numero = 1
        menor_numero = 10000000
        somatorio = 0
        qtd_numeros = 0
        soma_pares = 0

        while True:
            num = obter_numero_int_positivo('')
            qtd_numeros += 1
            somatorio += num
            if num % 2 == 0:
                soma_pares += num

            if num == 0:
                break
            elif num > maior_numero:
                maior_numero = num
            elif num < menor_numero:
                menor_numero = num
            else:
                continue


        media = somatorio / qtd_numeros

        print(f"""
        Maior número: {maior_numero} 
        Menor número: {menor_numero}
        Média: {media:.1f}
        Soma números pares: {soma_pares}
        """)
        
        contador -= 1
    

def limpar_tela():
    os.system('cls')

main()