import utils as u

def main():
    glicose = u.obter_num_float("Valor da glicose: ")

    classificacao = classificar_glicose(glicose)

    print(classificacao)


def classificar_glicose(glicose):
    
    if glicose < 100:
        return "\nA glicose está normal."
    elif glicose <= 125:
        return "\nVocê está com pré-diabetes."
    else:
        return "\nVocê está com diabetes."


main()