# frase = 'O Python é uma linguagem de programação ' \
# 'multiparadigma. ' \
# 'Python foi criado por Guido van Rossum.'
frase = 'aaaooo'

indice = 0  # é o índice usado para percorrer os caracteres da string (frase).

frequencia_maxima = 0 # armazena o maior número de vezes que uma letra aparece na frase.

letra_mais_frequente = ''  # guarda a letra que aparece mais vezes.

# Percorre cada caractere da frase
while indice < len(frase):  
    letra = frase[indice]

    # Ignora espaços em branco
    if letra == ' ':
        indice += 1
        continue

    # Conata a quantidade de vezes que a letra aparece na frase
    frequencia_atual = frase.count(letra)

    # Verifica se esta letra é a mais frequente
    if frequencia_maxima < frequencia_atual:
        frequencia_maxima = frequencia_atual
        letra_mais_frequente = letra
    
    indice += 1

print('A letra que apareceu mais vezes foi a letra ' 
      f'"{letra_mais_frequente.upper()}", que apareceu '
      f'{frequencia_maxima}x')