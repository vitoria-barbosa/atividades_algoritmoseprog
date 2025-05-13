# Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.

def main():
    print('-----MAIOR E MENOR NÚMERO-----')
    n1 = obter_numero_inteiro('Digite um número:')
    n2 = obter_numero_inteiro_diferente(n1)

    print(f'\n{maior_numero(n1,n2)} é o maior número')
    print(f'{menor_numero(n1,n2)} é o menor número')

def maior_numero(n1,n2):
   if n1 > n2:
      return n1
   else:
      return n2


def menor_numero(n1,n2):
   if n1 < n2:
      return n1
   else:
      return n2


def obter_numero_inteiro(label: str):
  return int(input(label))

def obter_numero_inteiro_diferente(n1):
    numero = obter_numero_inteiro('Digite outro número:')
    if n1 != numero:
        return numero
    else:
        print('\nOs números devem ser diferentes!')
        return obter_numero_inteiro_diferente(n1)

main()