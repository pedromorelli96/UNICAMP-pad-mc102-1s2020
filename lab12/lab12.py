def lista_moldurada(lista):
    # Primeira linha da moldura (numero de elementos + 2)
    print("." * (len(lista) + 2))

    # Linhas centrais (definido pelo maior elemento da lista)
    for i in range(int(max(lista)), 0, -1):
        print(".", end='')
        for x in lista:
            num = int(x)
            if (num >= i):
                print("|", end='')
            else:
                print(" ", end='')
        print(".")

    # Ultima linha da moldura
    print("." * (len(lista) + 2))

# Input #
entrada = input().split()
entrada_ordenada = sorted(entrada)

# Output #
lista_moldurada(entrada)

while (entrada != entrada_ordenada):
    for i in range (len(entrada)):
        # Verifica se ja estou olhando o ultimo elemento
        if (i == len(entrada) - 1):
            break

        # Converte os elementos para comparação (strings -> int)
        num1 = int(entrada[i])
        num2 = int(entrada[i+1])

        # Se o numero atual > numero na frente
        # Troque-os e printe o quadro
        if (num1 > num2):
            aux = entrada[i+1]
            entrada[i+1] = entrada[i]
            entrada[i] = aux
            lista_moldurada(entrada)
            

    



