# Leia 3 (três) números, verifique e escreva o maior entre os números lidos.

def main():
    n1 = obter_numero_inteiro('Digite um número:')
    n2 = obter_numero_inteiro('Digite outro número:')
    n3 = obter_numero_inteiro('Digite mais um número:')

    maior_numero(n1,n2,n3)

def maior_numero(n1,n2,n3):
   if n1 == n2 == n3:
       print('\nOs três números são iguais!')
   elif n1 > n2 and n1 > n3:
        print(f'\n{n1} é o maior número')
   elif n2 > n1 and n2 > n3:
       print(f'\n{n2} é o maior número')
   else:
       print(f'\n{n3} é o maior número')
    

def obter_numero_inteiro(label: str):
  return int(input(label))

main()