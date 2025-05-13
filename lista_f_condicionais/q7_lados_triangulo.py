# Leia 3 lados, verifique e escreva se os 3 lados formam um triângulo(a soma de dois lados não pode ser menor que o terceiro lado). Se formam, verifique se formam um triângulo equilátero, isósceles ou escaleno. Não existe lado com tamanho 0 (zero).

def main():
    print('Digite três valores para ver se formará um triângulo:\n')
    lado_a = obter_numero_inteiro_diferente_zero('Lado a: ')
    lado_b = obter_numero_inteiro_diferente_zero('Lado b: ')
    lado_c = obter_numero_inteiro_diferente_zero('Lado c: ')

    eh_triangulo(lado_a, lado_b, lado_c)

def eh_triangulo(a, b ,c):
   if a + b >= c and a + c >= b and b + c >= a:
    print('\nEsses lados formam um triângulo.')
    if eh_equilatero(a,b,c):
        print('Esse triângulo é equilátero, ou seja, tem os 3 lados iguais.')
    elif eh_isosceles(a,b,c):
        print('Esse triângulo é isósceles, ou seja, tem 2 lados iguais.')
    elif eh_escaleno(a,b,c):
        print('Esse triângulo é escaleno, ou seja, tem 3 lados diferentes.')
   else:
       print('\nEsses lados NÃO formam um triângulo!')

def eh_equilatero(a, b, c):
    return a == b == c

def eh_isosceles(a, b, c):
   return a == b or a == c or b == c

def eh_escaleno(a, b, c):
   return a != b and a != c and b != c

def obter_numero_inteiro_diferente_zero(label: str):
  num =  int(input(label))
  if num != 0:
     return num
  else:
     print('\nNão existe lado de tamanho 0.Tente outro valor!')
     return obter_numero_inteiro_diferente_zero(label)

main()