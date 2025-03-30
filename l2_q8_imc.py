# Escreva um programa que calcule o Índice de Massa Corporal (IMC), dado o peso e a altura.

# Entrada
peso = float(input('Digite seu peso(kg):'))
altura = float(input('Digite sua altura:'))

# Processamento
imc = peso / (altura ** 2)

# Saída
print('>>>> IMC (Índice de massa corporal) <<<<')
print(f'De acordo com seu peso {peso} e sua altura {altura}, seu IMC é = {imc:.2f}.')
