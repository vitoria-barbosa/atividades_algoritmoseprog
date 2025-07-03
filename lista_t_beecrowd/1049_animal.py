def main():
    animais = {
        "vertebrado": {
            "ave": {
                "carnivoro": "aguia", 
                "onivoro": "pomba"
            },
            "mamifero": {
                "onivoro": "homem",
                "herbivoro": "vaca"
            },
        },
        "invertebrado": {
            "inseto": {
                "hematofago": "pulga",
                "herbivoro": "lagarta"
            },
            "anelideo": {
                "hematofago": "sanguessuga",
                "onivoro": "minhoca"
            }
        }
    }

    osso = input()
    classe = input()
    alimentacao = input()

    print(animais[osso][classe][alimentacao])


main()