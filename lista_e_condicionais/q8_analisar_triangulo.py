from math import sqrt

def main():
    print('\n------ ANALISADOR DE TRIÂNGULOS ------')
    lado_a = obter_numero_inteiro_diferente_zero('Lado a: ')
    lado_b = obter_numero_inteiro_diferente_zero('Lado b: ')
    lado_c = obter_numero_inteiro_diferente_zero('Lado c: ')
    eh_triangulo(lado_a, lado_b, lado_c)


def eh_triangulo(lado_a, lado_b ,lado_c):
    if lado_a + lado_b >= lado_c and lado_a + lado_c >= lado_b and lado_b + lado_c >= lado_a:
      print('\nEsses lados formam um triângulo.')
    else:
        print('\nEsses lados não formam um triangulo. Fim.')


def classificar_pelos_lados(a, b, c):
   if a == b == c:
      return 'Equilátero'
   elif a == b or a == c or b == c:
      return 'Isósceles'
   else:
      return 'Escaleno'
   

def obter_numero_inteiro_diferente_zero(label: str):
  num =  int(input(label))
  if num != 0:
     return num
  else:
     print('\n0 não é um valor válido. Tente outro valor!')
     return obter_numero_inteiro_diferente_zero(label)
  
main()    