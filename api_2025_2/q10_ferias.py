from random import randint

def main():
    nome = input("Seu nome: ")

    mensagens = [f"Olá {nome}, aproveite suas férias mas também descanse bem!",
                f"Parabéns {nome}! Finalmente pode aproveitar suas férias.", 
                f"{nome}, descanse bastante e volte renovado para o próximo período!",
                f"Que suas férias sejam as melhores possíveis, {nome}!",
                f"Se for viajar {nome}, curta bastante e traga uma lembrança pra mim ok!",
                f"{nome}, por favor, não tranque o curso, você  é capaz de coisas incríveis!",
                f"Boas férias, {nome}!!!", 
                f"Parabéns {nome}, você  é uma potência da programação.",
                f"Desejo de coração que seus sonhos se realizem, {nome}!",
                f"Você é muito amado, {nome}, aproveite suas férias!"]

    aleatorio = randint(0, 9)

    print(mensagens[aleatorio])


main()