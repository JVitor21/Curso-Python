"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = int(input('Digite a velocidade: '))  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

VELOCIDADE_RADAR = 60  # velocidade máxima do radar 1
LOCAL_RADAR = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

# Verifica se a velocidade do carro excede a permitida pelo radar
velocidade_nao_permitida = velocidade > VELOCIDADE_RADAR

# Verifica se o carro está dentro do alcance do radar
passou_radar = local_carro >= (LOCAL_RADAR - RADAR_RANGE) and local_carro <= (LOCAL_RADAR + RADAR_RANGE)

if velocidade_nao_permitida and passou_radar:
    print('Multado')
else:
    print('Não multado')
