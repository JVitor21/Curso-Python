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
    except:
        numeros_validos = None

    # Se for None significa que os numeros são invalidos
    if numeros_validos is None:
        print('Um ou ambom os números digitados invalidos')
        continue
    
    if operador not in '+-*/**//%':
        print('Operador inválido!')
        continue
    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando a sua conta. Veja o resultado abaixo.')

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = ',num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = ', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = ', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = ', num_1_float * num_2_float)
    elif operador == '//':
        print(f'{num_1_float} // {num_2_float} = ', num_1_float // num_2_float)
    elif operador == '**':
        print(f'{num_1_float} ** {num_2_float} = ', num_1_float ** num_2_float)
    elif operador == '%':
        print(f'{num_1_float} % {num_2_float} = ', num_1_float % num_2_float)
    else:
        print('Nunca deveria chegar aqui.')
    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break