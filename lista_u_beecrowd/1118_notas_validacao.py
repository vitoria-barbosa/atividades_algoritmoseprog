def main():
    calcular_media()
    opcao()


def validar_nota():
    nota = float(input())

    if nota < 0 or nota > 10:
        print("nota invalida")
        return validar_nota()
    else:
        return nota
    

def calcular_media():
    nota1 = validar_nota()
    nota2 = validar_nota()

    media = (nota1 + nota2) / 2
    print(f"media = {media:.2f}")


def opcao():
    print("novo calculo (1-sim 2-nao)")
    escolha = int(input())
    if escolha != 1 and escolha != 2:
        return opcao()
    if escolha == 1:
        calcular_media()
        opcao()
    else:
        return
    
main()