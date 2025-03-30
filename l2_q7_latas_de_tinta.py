# Escreva um programa que calcule quantas latas de tinta são necessárias para pintar uma área.

# Entrada
area = float(input('Tamanho da área a ser pintada em m²:'))
lata_de_tinta = float(input('Quantos m² uma lata de tinta cobre:'))

# Processamento
quantidade_latas = area / lata_de_tinta

# Saída
print(f'Para uma área de {area} m², serão necessárias {quantidade_latas:.1f} latas de tinta.')
