# Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$).

# Entrada
dolar = float(input('Quanto está o dólar hoje: '))
valor = float(input('Digite o valor que você quer converter: '))

# Processamento
real = dolar * valor

# Saída
print('------- DÓLAR >> REAL -------')
print(f' $ ={valor:.2f}')
print(f'R$ ={real:.2f}')
