"""Cauculadora com while"""

while True:
    primeiro_valor = input('Digite o primerio valor: ')
    operador = input('Digite um operador: ')
    segundo_valor = input('Digite o segundo valor: ')

    num_1_float = 0
    num_2_float = 0

    numeros_validos = None
    
    try:
        num_1_float = float(primeiro_valor)
        num_2_float = float(segundo_valor)
        numeros_validos = True
    except ValueError:
        numeros_validos = None  # Se for None significa que os numeros são invalidos

   #Verifica se os numeros são validos, se não for, exibe a mesnagem e usa o "continue" para reiniciar o laço
    if numeros_validos is None:
        print('Um ou ambom os números digitados invalidos')
        continue
    
    if operador not in '+-*/**//%':
        print('Operador inválido!')
        continue

    print('Realizando a sua conta. Veja o resultado abaixo.')
    try:
        if operador == '+':
            print(f'{int(num_1_float)} + {int(num_2_float)} = {int(num_1_float + num_2_float)}')
        elif operador == '-':
            print(f'{int(num_1_float)} - {int(num_2_float)} =  {int(num_1_float - num_2_float)}')
        elif operador == '/':
            print(f'{int(num_1_float)} / {int(num_2_float)} = {int(num_1_float / num_2_float)}')
        elif operador == '*':
            print(f'{int(num_1_float)} * {int(num_2_float)} = {int(num_1_float * num_2_float)}')
        elif operador == '//':
            print(f'{int(num_1_float)} // {int(num_2_float)} = {num_1_float // num_2_float}')
        elif operador == '**':
            print(f'{int(num_1_float)} ** {int(num_2_float)} = {num_1_float ** num_2_float}')
        elif operador == '%':
            print(f'{int(num_1_float)} % {int(num_2_float)} = {num_1_float % num_2_float}')
        else:
            print('Nunca deveria chegar aqui.')
    except ZeroDivisionError:
        print('Erro: Proibido divisão por 0')
    # O método lower converte todos os caracteres alfabéticos de uma string para letras minúsculas.
    entrada = input('Quer sair? [s]im ou [n]ão: ').lower()

    # O método startswith verifica se uma string começa com um determinado prefixo ou sequência de caracteres.
    if entrada.startswith('s'):
        print('Saindo...')
        break
    elif entrada.startswith('n'):
        print('Voçê escolheu não sair!')
    else:
        print('Entrada invalida, teste novamente!')