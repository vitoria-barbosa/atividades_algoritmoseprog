# Leia 3 (três) números e escreva-os em ordem crescente com condicional.

def main():
    print('Digite três números para colocá-los em ordem crescente:\n')
    n1 = obter_numero_inteiro('Número 1: ')
    n2 = obter_numero_inteiro('Número 2: ')
    n3 = obter_numero_inteiro('Número 3: ')

    print(f'\nOrdem crescente: {num_menor(n1,n2,n3)}, {num_meio(n1,n2,n3)}, {num_maior(n1,n2,n3)}')


def num_menor(n1,n2,n3):
    if n1 <= n2 and n1 <= n3:
     return n1
    elif n2 <= n1 and n2 <= n3:
      return n2
    else:
     return n3
    
    
def num_maior(n1,n2,n3):
   if n1 >= n2 and n1 >= n3:
    return n1
   elif n2 >= n1 and n2 >= n3:
    return n2
   else:
    return n3
   

def num_meio(n1,n2,n3):
    if num_menor(n1,n2,n3) < n1 < num_maior(n1,n2,n3):
      return n1
    elif num_menor(n1,n2,n3) < n2 < num_maior(n1,n2,n3):
      return n2
    else:
      return n3
  

def obter_numero_inteiro(label: str):
  return int(input(label))    

main()