"""
Exercicio da aula 47 diferente do professor
"""
import os

palavra_secreta = 'Joaninha'
letras_acertadas = ['*'] * len(palavra_secreta) #aqui deixa tudo como * de inicio
contador = 0

print('Vamos começar o jogo!\n')

while True:
    print('Palavra:', ''.join(letras_acertadas)) # Mostra o estado atual da palavra com letras descobertas e *
    letra_usuario = input('Digite uma letra: ')
    contador += 1

    try:
        if len(letra_usuario) > 1:
            print('Digite apenas uma letra!')
            continue

        if letra_usuario.isdigit():
            print('Digite apenas letras!')
            continue

        if letra_usuario.lower() in palavra_secreta.lower():

            # atualiza a lista de letras acertadas
            for indice, letra in enumerate(palavra_secreta):
                if letra.lower() == letra_usuario.lower():
                    letras_acertadas[indice] = letra # subtitui * pela letra correta


            # verifica se todas as letras foram descobertas
            if '*' not in letras_acertadas:
                os.system('cls')
                print('PARABÉNS VOCÊ COSNEGUIU!!!')
                print(f'Você descobriu a palavra: {palavra_secreta}!')
                print(f'Você tentou {contador}x')
                break
        else:
            print('Não foi dessa vez, tente de novo!')
            continue
    except:
        print('NÃO DEVE CHEGAR AQUI!')
