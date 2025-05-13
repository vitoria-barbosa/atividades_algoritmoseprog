# Leia uma letra, verifique se letra é "F" ou "M" e escreva F - Feminino, M - Masculino, Sexo Inválido.
def main():
    obter_sexo_valido()


def obter_sexo_valido():
    sexo = input('Digite um sexo(F para feminino e M para masculino): ')
    if sexo == 'F':
        print('\nF - Feminino')
        return sexo
    elif sexo == 'M':
        print('\nM - Masculino')
        return sexo
    else:
        print('\nSexo Inválido. Tente novamente!')
        return obter_sexo_valido()

main()