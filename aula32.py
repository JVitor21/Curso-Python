"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
    # recebe um número inteiro
    num_int = int(input('Digiteum número inteiro: '))

    # verifica se é impar ou par
    if num_int %2 == 0 and num_int is not int:
        print(f'o número {num_int} é par')
    else:
        print(f'O número {num_int} é impar')

except ValueError:
    # se não for inteiro, joga um erro
    print("O valor inserido não é um número interiro!")
    
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = int(input('Que horas são? '))

# verifica se o numero esta entre 0 ou 23
try:
    if 0 <= hora <= 23:
        # exibe a saudação apropriada
        if 5 <= hora <= 11:
            print('Bom dia!')
        elif 12 <= hora <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite')
    else:
        print('Horario invalido. Por favor, insira um horario valido entre 0 e 23')
except ValueError:
    print('O valor inserido não é uma hora valida!')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Insira seu primeiro nome: ')

# verifica o tamanho do nome e exibe a saudação apropriada
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print(f'{tamanho_nome}, seu nome é curto!')
    elif 5 <= tamanho_nome <= 6:
        print(f'{tamanho_nome}, seu nome é normal!')
    else:
        print(f'{tamanho_nome}, seu nome é muito grande!')
else:
    print('Digite mais de uma letra!')