def main():
    print('-----VERIFICADOR DE ANO BISSEXTO-----\n')
    ano = obter_ano('Digite um ano: ')
    if eh_bissexto(ano):
        print(f'\n{ano} é ano bissexto!')
    else:
        print(f'\n{ano} não é bissexto.')


def eh_bissexto(ano: int):
  return (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0


def obter_ano(label: str): # só permite anos de 4 digitos
    ano = int(input(label))
    if ano / 1000 >= 1 and ano / 1000 < 10:
        return ano
    else:
        print(f'{ano} não é valido. Digite um ano de 4 dígitos.')
        return obter_ano(label)

main()