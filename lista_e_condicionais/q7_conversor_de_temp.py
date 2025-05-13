def main():
    print('\n--CONVERSOR DE TEMPERATURA (KELVIN,FAHRENHEIT E CELSIUS)--')
    escala1 = obter_escala_com_validacao('Escala que quer converter(F,C,K): ')
    temperatura = obter_temperatura_e_validar(escala1)
    escala2 = obter_escala_com_validacao('Escala a ser convertido(F,C,K): ')
    temperatura_convertida = converter_temperatura(temperatura, escala1, escala2)
    print(f'\n{temperatura:.2f}°{escala1} corresponde a {temperatura_convertida:.2f}°{escala2}')

    
def converter_temperatura(temp, escala1, escala2):
    if escala1 == 'c' and escala2 == 'f':
        return ((temp * 9) / 5) + 32
    elif escala1 == 'c' and escala2 == 'k':
        return temp + 273
    elif escala1 == 'f' and escala2 == 'c':
        return ((temp - 32) * 5) / 9
    elif escala1 == 'f' and escala2 == 'k':
        return ((temp + 459.67) * 5) / 9
    elif escala1 == 'k' and escala2 == 'f':
        return ((temp - 273.15) * 1.8) + 32
    elif escala1 == 'k' and escala2 == 'c':
        return temp - 273
    

def obter_temperatura_e_validar(escala):
    temperatura = float(input('Digite a temperatura que quer transformar: '))
    if escala == 'k':
        if temperatura < 0:
            print('Temperatura inválida! Não há valores negativos em kelvin. Tente novamente:')
            return obter_temperatura_e_validar(escala)
        else:
            return temperatura
    elif escala == 'c':
        if temperatura < -273.15:
            print('Temperatura inválida! Não há temperaturas menores que -273.15 em Celsius.Tente novamente:')
            return obter_temperatura_e_validar(escala)
        else: 
            return temperatura
    else:
        return temperatura


def obter_escala_com_validacao(label):
    escala =  str(input(label))
    if escala == 'f' or escala == 'c' or escala == 'k':
        return escala
    else:
        print('Escala inválida. Digite f para fahrenheit, c para Celcius e k para Kelvin.Tente novamente:')
        return obter_escala_com_validacao('Escala que quer converter(F,C,K): ')

main()