"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
contador = 0
print('Contagem: ')

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Não vou mstar o 6.')
        continue #pula o laço, volta e continua de onde parou

    if contador >= 10 and contador <=27:
        print('Não vou mostar o ', contador)
        continue
    
    print(contador)
    
    if contador == 40:
        break
    
print('Acabou')
