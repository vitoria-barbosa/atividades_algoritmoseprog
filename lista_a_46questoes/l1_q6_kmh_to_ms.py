# 6. Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s.

# Entrada
kmh = int(input('Quantidade de quilômetros por hora:'))

# Processamento
ms = kmh / 3.6

# Saída
print(f'{kmh} Km/h equivalem a {ms:.1f} m/s!')
