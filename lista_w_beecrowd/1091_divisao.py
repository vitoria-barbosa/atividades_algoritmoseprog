# A entrada contém vários casos de teste. A primeira linha de um caso de teste contém um inteiro K indicando o número de consultas que serão realizadas (0 < K ≤ 103). A segunda linha de um caso de teste contém dois números inteiros N e M representando as coordenadas do ponto divisor (-104 < N, M < 104). Cada uma das K linhas seguintes contém dois inteiros X e Y representando as coordenadas de uma residência (-104 ≤ X, Y ≤ 104).Em todas as coordenadas dadas, o primeiro valor  corresponde à direção leste-oeste, e o segundo valor corresponde à direção norte-sul.
# O final da entrada é indicado por uma linha que contém apenas o número zero.
# Saída
# Para cada caso de teste da entrada seu programa deve imprimir uma linha contendo:
# a palavra divisa se a residência encontra-se em cima de uma das linhas divisórias (norte-sul ou leste-oeste);
# NO se a residência encontra-se na Nlogônia do Noroeste;
# NE se a residência encontra-se na Nlogônia do Nordeste;
# SE se a residência encontra-se na Nlogônia do Sudeste;
# SO se a residência encontra-se na Nlogônia do Sudoeste.
def main():
    while True:

        n = int(input())

        if n == 0:
            break
        
        leste_oeste, norte_sul = map(int, input().split())

        for i in range(n):
            
            coordenada1, coordenada2 = map(int, input().split())

            if coordenada1 == leste_oeste or coordenada2 == norte_sul:
                print("divisa")

            elif coordenada1 < leste_oeste and coordenada2 > norte_sul:
                print("NO")
            
            elif coordenada1 > leste_oeste and coordenada2 > norte_sul:
                print("NE")

            elif coordenada1 > leste_oeste and coordenada2 < norte_sul:
                print("SE")

            else:
                print("SO")


main()