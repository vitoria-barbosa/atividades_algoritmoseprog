# Escreva um programa que aplique um desconto percentual sobre um preço inicial.

# Entrada
valor_inicial = float(input('Valor inicial do produto:'))
porcentagem_desconto = int(input('Porcentagem do desconto a ser aplicado:'))

# Processamento
desconto = ((100 - porcentagem_desconto) / 100) * valor_inicial

# Saída
print(f'O produto que custava {valor_inicial:.2f}, com um desconto de {porcentagem_desconto}%, passará a custar {desconto:.2f}')
