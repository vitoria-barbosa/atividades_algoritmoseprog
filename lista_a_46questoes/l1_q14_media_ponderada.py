# 14. Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada.

# Entrada
nota1 = float(input('Nota 1:'))
peso1 = int(input('Peso da nota 1:'))
nota2 = float(input('Nota 2:'))
peso2 = int(input('Peso da nota 2:'))
nota3 = float(input('Nota 3:'))
peso3 = int(input('Peso da nota 3:'))

# Processamento
media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 +peso3)

# Saída
print(f'Considerando as notas obtidas e os pesos correspondentes, a média desse aluno ficou {media_ponderada:.1f}.')
