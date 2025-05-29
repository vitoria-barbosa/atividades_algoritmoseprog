from utils import obter_num_inteiro

def main():
    print('---- NÚMEROS PRIMOS----')
    limite_inferior = obter_num_inteiro('Limite Inferior: ')
    limite_superior = obter_num_inteiro('Limite Superior: ')
    print(f'\nEntre {limite_inferior} e {limite_superior} esses são os números primos:')

    for i in range(limite_inferior, limite_superior+1, 1):
        if i <= 1:
            continue
        eh_primo = True
        for divisores in range(2, int(i ** 0.5) + 1, 1):
            if i % divisores == 0:
                eh_primo = False
                break
        if eh_primo:
            print(i)

    print('Fim.')

main()