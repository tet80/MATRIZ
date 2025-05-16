# INICIALIZANDO UMA LISTA DE LISTAS CHAMADA MATRIZ PARA REPRESENTAR A MATRIZ 4X4
# CADA LISTA INTERNA REPRESENTA UMA LINHA DA MATRIZ, INICIALIZNADO COM 4 ZEROS 
MATRIZ = [[0] *4 for _ in range(4)]

# PREENCHE a LINHA DE ÍNDICE 0 DA MATRIZ:
# Atribui o valor 0 ao elemento na linha 0, coluna 0
MATRIZ[0][0] = 0
# Atribui o valor 1 ao elemento na linha0,  coluna 1
MATRIZ[0][1] = 1
# Atribui o valor 0 ao elemento na linha 0, coluna 2
MATRIZ[0][2] = 0
 # Atribui o valor 1 ao elemento na linha 0,coluna 3
MATRIZ[0][3] = 1
# Preenche a linha de índice 1 da matriz:
# Atribui o valor 0 ao elemento na linha 1, coluna 0
MATRIZ[1][0] = 0
# Atribuí o valor 0 ao elemento na linha 1, coluna 1
MATRIZ[1][1] = 0
# Atribuí o valor 1 ao elemento ma linha 1, coluna 2
MATRIZ[1][2] = 1
# Atribuí o valor 0 ao elemento na linha 1, coluna 3
MATRIZ[1][3] = 0

# Exibindo os valores da matriz:
# Loop externo para para percorrer os índices das linhas (de 0 a 3)
for contradort in range(4):
    # Loop interno para percorrer os índices das colunas 
