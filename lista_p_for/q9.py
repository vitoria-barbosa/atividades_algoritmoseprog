from utils import obter_num_inteiro

def main():
    print('---- NÚMEROS PARES----')
    limite_inferior = obter_num_inteiro('Limite Inferior: ')
    limite_superior = obter_num_inteiro('Limite Superior: ')
    print(f'\nEntre {limite_inferior} e {limite_superior} esses são os números pares:')
    
    for i in range(limite_inferior, limite_superior+1, 1):
        if i % 2 == 0:
            print(i)

main()