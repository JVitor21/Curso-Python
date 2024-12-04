"""
Iteravel -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue o seu iterador
"""
# Criar o iterador
# texto = iter('Luiz')  # __iter__()

# Usar o método __next__() para obter os elementos
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print(next(texto))

# Tentando avançar além dos elementos
# print(texto.__next__())  # Levanta StopIteration

# for letra in texto
texto = 'Luiz' # iteravel
# iterador = iter(texto) # iterador

# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

# o codigo anterior faz isso
for letra in texto:
    print(letra)