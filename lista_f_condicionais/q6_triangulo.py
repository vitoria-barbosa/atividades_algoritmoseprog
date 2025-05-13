# Leia 3 (três) ângulos, verifique e escreva se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180o). Se formam, verifique se formam um triângulo acutângulo, retângulo ou obtusângulo. Não existe ângulo com tamanho 0o (zero grau).

def main():
    angulo1 = obter_numero_inteiro_diferente_zero('Digite um ângulo: ')
    angulo2 = obter_numero_inteiro_diferente_zero('Digite outro ângulo: ')
    angulo3 = obter_numero_inteiro_diferente_zero('Digite outro ângulo: ')

    eh_triangulo(angulo1, angulo2, angulo3)

def eh_triangulo(a1,a2,a3):
   if a1 + a2 + a3 == 180:
    print('\nEsses ângulos formam um triângulo')
    if eh_acutangulo(a1,a2,a3):
      print('Esse triângulo é um acutângulo!')
    elif eh_retangulo(a1,a2,a3):
      print('Esse triângulo é retângulo!')
    elif eh_obtusangulo(a1,a2,a3):
      print('Esse triângulo é obtusângulo!')
   else:
        print('\nEsses ângulos NÃO formam um triângulo')
      

def eh_acutangulo(a1,a2,a3):
   """verifica se os tres ângulos do triângulo são menores de 90° graus"""
   return a1 < 90 and a2 < 90 and a3 < 90


def eh_retangulo(a1,a2,a3):
  """verifica se algum dos ângulos do triângulo é igual a 90° graus"""
  return a1 == 90 or a2 == 90 or a3 == 90
   

def eh_obtusangulo(a1,a2,a3):
  """verifica se algum dos ângulos do triângulo é maior 90° graus"""
  return a1 > 90 or a2 > 90 or a3 > 90
    

def obter_numero_inteiro_diferente_zero(label: str):
  num =  int(input(label))
  if num != 0:
     return num
  else:
     print('\nNão existe angulo de 0°.Tente outro angulo!')
     return obter_numero_inteiro_diferente_zero(label)

main()