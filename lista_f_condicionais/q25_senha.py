# Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. O algoritmo deve escrever
# uma mensagem de permissão de acesso ou não.
def main():
    obter_senha_numerica_correta()

def obter_senha_numerica_correta():
    entrada = input('Digite a senha: ')
    if len(entrada) > 4 or len(entrada) < 4:
        print('A senha tem 4 números. Tente novamente: ')
        return obter_senha_numerica_correta()
    try:
        senha = int(entrada)
        if senha == 1234:
            print('Senha corrteta!')
        else:
            print('Senha incorreta. Tente novamente: ')
            return obter_senha_numerica_correta()
    except ValueError:
        print('A senha é númerica e inteira. Tente novamente!')
        return obter_senha_numerica_correta()

main()