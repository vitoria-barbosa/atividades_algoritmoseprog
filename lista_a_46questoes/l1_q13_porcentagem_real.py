# 13. Leia um valor em real (R$), calcule e escreva 70% deste valor.

# Entrada
real = float(input('Digite um valor em real(R$):'))

# Processamento
porcentagem = (70 * real) / 100

# Saída
print(f'70% de {real:.2f} corresponde a {porcentagem:.2f}')
