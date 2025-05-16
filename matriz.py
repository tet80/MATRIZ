MATRIZ = [[0] * 4 for _ in range(4)]

MATRIZ[0][0] = 0
MATRIZ[0][1] = 1
MATRIZ[0][2] = 0
MATRIZ[0][3] = 1
MATRIZ[1][2] = 1
MATRIZ[1][3] = 0

# Substitui o uso errado de input() por uma entrada válida
for contador1 in range(4):
    for contador2 in range(4):
        valor = int(input(f"Digite o valor para posição [{contador1}][{contador2}]: "))
        MATRIZ[contador1][contador2] = valor

# Exibe a matriz
for contador1 in range(4):
    for contador2 in range(4):
        print(MATRIZ[contador1][contador2], end=" ")
    print()

