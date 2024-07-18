# É usado para exibir coisas na tela e recebe um ou mais argumentos
# Ele recebe argumentos, nomeados ou não
# print(12,34) não nomeado
print(12,34)
# print(56,78, sep='-') nomeado
print(56,78, sep="-") # sep='' -> argumento nomeado separador
# \r\n -> CRLF -> IUNIX
# \n -> LF -> Windows
print(9, 10, sep="-", end='##')
# argumento nomeado end='' -> final de linha, tira a quebra de linha
print(11, 12, sep="-", end='##\n')
print(13, 14, sep="-", end='\n##')