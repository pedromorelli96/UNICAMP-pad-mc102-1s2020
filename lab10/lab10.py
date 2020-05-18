# Função que verifica se o caracter é igual a '@'
# Se sim, retorna 1
def celula_viva(c):
    if (c == "@"):
        return 1
    else:
        return 0

# Biblioteca padrão sys para usar sys.stdin.readlines()
import sys
import copy

# Leitura através de sys.stdin.readlines()
# Remove '\n' no final de cada linha através de rstrip()
entrada = [line.rstrip() for line in sys.stdin.readlines()]

# Verifica se leu alguma linha em branco
# Se sim, remove a linha em branco
if (entrada[-1] == ''):
    entrada.pop(-1)

# Guarda os passos do ultimo elemento lido
num_passos = int(entrada[-1])
# print(num_passos)

# Atualiza a entrada para conter apenas a moldura
entrada.pop(-1)

# Cria nova lista que copia a entrada
diagrama_aux = entrada.copy()

# Modifica os elementos da lista auxiliar que são strings para listas
# criando uma lista de listas que pode ser alterada
diagrama = []
for x in diagrama_aux:
    linha = list(x)
    diagrama.append(linha)

# Primeira saída requerida
# Moldura da entrada igual
for x in entrada:
    print(x)

for i in range(0, num_passos):
    # Cria outro diagrama que irá receber as alterações da logica
    diagrama_saida = copy.deepcopy(diagrama)

    # i itera sobre cada linha do diagrama
    # A primeira e última linha são molduras (não conta 0 e -1)
    # As células adjacentes à moldura estão sempre mortas (não conta 1 e -2)
    # Desta forma, começamos do indice 2, até o ultimo indice -2
    for i in range(2, len(diagrama) - 2):
        # j itera sobre cada caracter de cada linha
        # O primeiro e último caracter são parte da moldura (não conta 0 e -1)
        # Os caracteres adjacentes à moldura estão sempre mortos (não conta 1 e -2)
        for j in range(2, len(diagrama[i]) - 2):
            # diagrama[i][j] corresponde aos caracteres (' ' ou '@') que podem ser alterados
            
            # Agora, precisamos olhar os oito caracteres vizinhos ao caracter atual [i][j]
            # São eles (sentido horário):
            # v1 = [i-1][j]
            # v2 = [i-1][j+1]
            # v3 = [i][j+1]
            # v4 = [i+1][j+1]
            # v5 = [i+1][j]
            # v6 = [i+1][j-1]
            # v7 = [i][j-1]
            # v8 = [i-1][j-1]

            num_vizinhos = 0

            for k in range(-1, 2):
                for l in range(-1, 2):
                    # Nesse caso, estamos na celula atual
                    # Não queremos contar essa
                    if ((k == 0) and (l == 0)):
                        num_vizinhos += 0
                    else:

                        if (celula_viva(diagrama[i+k][j+l]) == 1):
                            
                            num_vizinhos += 1
                            

            # Precisamos saber se a celula atual esta viva ou morta para aplicar a logica:
            # - Sobrevivencia : toda célula viva com 2 ou 3 vizinhos sobrevive
            # - Morte : toda célula com 4 ou mais vizinhos morre
            #           toda célula com menos de 2 vizinhos morre
            # - Nascimento : uma célula morta (re)nasce se tiver exatamente 3 vizinhos

            # Quer dizer que a celula atual está viva 
            if (celula_viva(diagrama[i][j]) == 1):
                if (num_vizinhos >= 4):
                    # Morte
                    diagrama_saida[i][j] = ' '
                elif (num_vizinhos < 2):
                    # Morte
                    diagrama_saida[i][j] = ' '
            # No caso que a celula atual não está viva        
            else:
                if (num_vizinhos == 3):
                    # Renasce
                    diagrama_saida[i][j] = '@'

    for x in diagrama_saida:
        for y in x:
            print(y, end='')
        print()

    diagrama = copy.deepcopy(diagrama_saida)

