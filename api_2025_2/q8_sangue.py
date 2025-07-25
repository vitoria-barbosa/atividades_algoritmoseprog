import utils as u

def main():
    print("Quer doar sangue?\n")
    idade = u.obter_num_int("Sua idade: ")
    peso = u.obter_num_float("Seu peso: ")

    if esta_apto(idade, peso):
        print("\nParabéns, você está apto(a) para doar!!")
    else:
        print("\nInfelizmente você não está apto(a) para doar.")


def esta_apto(idade, peso):
    return 18 <= idade <= 60 and peso >= 50


main()