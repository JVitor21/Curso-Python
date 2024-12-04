# senha_salva = '123456'
# senha_digitada = ''
# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(f'Número de repetições: {repeticoes}')
# print('Aquele laço acima pode ter repetições infinitas!')

texto = 'Python'

novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print('\n')
print(novo_texto)