"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'Joaninha'
letras_acertadas = ''
numero_tentativas = 0

print('Vamos começar o jogo!\n')

while True:
    # add 1 ao numero_tentativas cada vez que um caractere e digitado
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    try:
        # se for digitado mais de uma letra, printa a mensagem e continua
        if len(letra_digitada) > 1:
            print('Digite apenas uma letra!')
            continue
        else:
            print('Vamos lá de novo!')

        # se for digitado um digito, printa a resposta e continua
        if letra_digitada.isdigit():
            print('Digite apenas letras!')
            continue

        # se for digitado uma letra que contenha na palavra_secreta, você acerta e acaba
        if letra_digitada.lower() in palavra_secreta.lower():
            letras_acertadas += letra_digitada

        palavra_formada = ''
        for letra_secreta in palavra_secreta.lower():
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += '*'

        print(f'Palavra formada: {palavra_formada}')

        if palavra_formada == palavra_secreta.lower():
            os.system('cls')
            print('VOCÊ GANHOU!!! PARABÉNS!!!!')
            print(f'A palavra era: "{palavra_secreta}"')
            print(f'Número de tentativas: "{numero_tentativas}"')
            letras_acertadas = ''
            numero_tentativas = 0
            break
    except:
        print('NÃO DEVE CHEGAR AQUI!')