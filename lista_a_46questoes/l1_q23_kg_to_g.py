# Leia um valor em kg (quilograma), calcule e escreva o equivalente em g (grama).

def principal():
    kg = float(input('Digite um valor em Kg: '))
    gramas = kg * 1000

    print(f'>>> {kg} quilogramas equivalem a {gramas:.0f} gramas.')

principal()
