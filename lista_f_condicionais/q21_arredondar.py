# Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for
# maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso
# contrario, é arredondado para o inteiro imediatamente inferior.
from package.io_utils import obter_numero_float
def main():
    num = obter_numero_float('Digite o número que quer arrendondar: ')
    inteiro = num // 1
    decimal = num % 1
    if decimal >= 0.5:
        print(inteiro + 1)
    else:
        print(inteiro - 1)
        
main()