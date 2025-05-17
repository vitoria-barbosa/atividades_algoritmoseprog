# Seu objetivo portanto é fazer um Gerador de Senhas com as
# seguintes regras:
# - Numérica com tamanho fixo de N dígitos
# - Não deve permitir que o digital atual seja igual ao anterior
# - Não pode também ser antecessor ou sucessor imediato.
# - O usuário vai pedir uma senha, e então você deve mostrar a
# senha sugerida seguindo as regras.
# - E então perguntar se ele está satisfeito com a senha
# gerada. Caso negativo, gerar nova senha. Continue assim
# até ele ficar satisfeito.
from random import randint
def main():
    print("====== CRIADOR DE SENHAS =======")
    tamanho = int(input("Tamanho da senha: "))
    senha = gerar_senha(tamanho)
    print(f'\nSenha >> {senha}')

    gostou = int(input("\nVocê gostou? 1 - Sim, 2 - Não: "))

    while gostou != 1:
        senha = gerar_senha(tamanho)
        print(f'\nSenha >> {senha}\n')
        gostou = int(input('Você gostou? 1 - Sim, 2 - Não: '))
  
    print('\nQue bom que você gostou!')
    print('Fim.')


def gerar_senha(tamanho: int):
  senha = ''
  anterior = ''
  while len(senha) < tamanho:
    atual = str(randint(0, 9))

    if anterior == '' or (atual != anterior and diferenca(atual, anterior) > 1):
      anterior = atual
      senha += atual
  
  return senha


def diferenca(valor1: str, valor2: str) -> int:
  a = int(valor1)
  b = int(valor2)

  diff = a - b

  if a >= b:
    return diff
  else:
    return -1 * diff

main()