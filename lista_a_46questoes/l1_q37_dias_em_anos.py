# Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

def principal():
    dias = int(input('Digite sua idade em dias: ')) 
    anos = dias // 365
    meses = (dias % 365) // 30
    dias_restantes = (dias % 365) % 30

    print(f'Sua idade de {dias} dias, corresponde aproximadamente a {anos} anos, {meses} meses e {dias_restantes} dias.')

principal()
