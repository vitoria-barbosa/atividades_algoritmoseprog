# feita pelo professor Rogério

def main():
  senha = input('Senha: ')

  if eh_senha_valida(senha):
    print('Ok. Senha atende aos critérios')
  else:
    print('Senha NÃO atende ao critérios')


def eh_senha_valida(senha): # \ indica para o python que continua na próxima linha, usado para organizar o código
  if len(senha) >= 8 \
    and contem_letra_maiscula(senha) \
      and contem_letra_minuscula(senha) \
        and contem_numero(senha) \
          and contem_especial(senha):
            return True
  
  return False



def contem_letra_minuscula(senha): # usa recursividade para percorrer a senha
  if len(senha) == 0: # caso simple/parada>> Se a string estiver vazia, significa que não foi encontrada nenhuma letra minúscula até o momento
    return False

  if eh_minusculo(senha[0]): 
    return True
  
  return contem_letra_minuscula(senha[1:]) # verifica se o caractere 0 da senha é minusculo, senão for, a função chama a si mesma de novo, mas com o restante da senha (ou seja, sem o primeiro caractere).


def contem_letra_maiscula(senha):
  # Operador Ternário Python (ler)
  return False if len(senha) == 0 else eh_maiusculo(senha[0]) or contem_letra_maiscula(senha[1:])


def contem_numero(texto):
  if len(texto) == 0:
    return False

  if eh_numero(texto[0]):
    return True 

  return contem_numero(texto[1:]) 


def contem_especial(texto):
  if len(texto) == 0:
    return False
  
  if eh_especial(texto[0]):
    return True
  
  return contem_especial(texto[1:])


def eh_maiusculo(caracter):
  return ord(caracter) >= 65 and ord(caracter) <= 90


def eh_minusculo(caracter):
  return ord(caracter) >= 97 and ord(caracter) <= 122


def eh_numero(caracter):
  return ord(caracter) >= 48 and ord(caracter) <= 57


def eh_especial(caracter):
  return caracter in '!@#$%ˆ&*()_+'


main()