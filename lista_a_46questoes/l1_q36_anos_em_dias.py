# Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.

def principal():
    print('Digite sua idade em: ')
    anos = int(input('Anos: ')) 
    meses = int(input('Meses: '))
    dias = int(input('Dias: '))
    idade_em_dias = (anos * 365) + (meses * 30) + dias

    print(f'Sua idade de {anos} anos, {meses} meses e {dias} dias corresponde aproximadamente a {idade_em_dias} dias de vida.')

principal()
