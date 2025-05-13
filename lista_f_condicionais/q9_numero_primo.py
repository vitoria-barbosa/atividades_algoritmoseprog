# Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.

def main():
    num = obter_numero_entre_um_e_cem('Digite um número de 0 a 100: ')
    eh_primo(num)


def eh_primo(n):
    if n == 2:
     print(f'{n} é primo')
    elif n == 1:
        print(f'{n} não é primo.')
    else:
     for i in range(2, n + 1):
        if n % i == 0:
            return print(f'\n{n} não é primo')
        else:
            return print(f'\n{n} é primo')


def obter_numero_entre_um_e_cem(label: str):
  numero = int(input(label))
  if 1 <= numero <= 100:
     return numero
  else:
     print('\nDeve ser um número entre 1 e 100.Tente novamente:')
     return obter_numero_entre_um_e_cem(label)

main()