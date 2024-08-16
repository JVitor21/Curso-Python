primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')


if primeiro_valor > segundo_valor:
    print('O primeiro valor', primeiro_valor, 'é maior que', 'o segundo_valor ', segundo_valor)
elif segundo_valor > primeiro_valor:
    print('O segundo valor', segundo_valor, 'é maior que ', 'o primeiro valor', primeiro_valor)
elif primeiro_valor == segundo_valor or segundo_valor == primeiro_valor:
    print('Os valores são iguais!')
else:
    print('Os valores são diferentes!')
    