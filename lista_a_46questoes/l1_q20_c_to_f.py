# 20. Leia uma temperatura em °C, calcule e escreva a equivalente em °F. (t°F = (9 * t°C + 160) / 5)

# Entrada
celcius = int(input('Temperatura em °C:'))

# Processamento
f = (9 * celcius + 160) / 5

# Saída
print(f'{celcius} °C equivalem a {f:.1f} °F')
