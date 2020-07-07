def busca_binaria(lista, i_central, procurado):
    if (lista[i_central] == procurado):
        return lista, lista[i_central]
    else:
        if (procurado < lista[i_central]):
            lista_r = []
            for x in range(i_central):
                lista_r.append(lista[x])
            return lista_r, -1
        else:
            lista_r = []
            for x in range(i_central + 1, len(lista)):
                lista_r.append(lista[x])
            return lista_r, -1

def get_central(lista):
    # Se houver um número par de elementos
    if (len(lista) % 2 == 0):
        i_central = int((len(lista)/2)) - 1
    # Caso o número de elementos seja ímpar
    else:
        i_central = int((len(lista)/2))

    return i_central

def lista_moldurada(lista, marcador_central, lista_copia):
    # Verifica se é o print da lista inicial ou não
    if (marcador_central):
        i_central = get_central(lista)

        # Calculo dos espaços necessários (se for o caso)
        # Se a lista atual for a mesma que a original, não há espaços
        if (len(lista) == len(lista_copia)):
            # Primeira linha da moldura
            print("+", end='')
            for i in range(len(lista)):
                if (i == i_central):
                    print("=====+", end='')
                else:
                    print("-----+", end='')
            print()

            # Linha central
            print("|", end='')
            for i in range(len(lista)):
                if (i == i_central):
                    print("|", end='')
                    print(str(lista[i]).zfill(3), end='')
                    print("||", end='')
                else:
                    print(" ", end='')
                    print(str(lista[i]).zfill(3), end='')
                    print(" |", end='')
            print()

            # Ultima linha da moldura
            print("+", end='')
            for i in range(len(lista)):
                if (i == i_central):
                    print("=====+", end='')
                else:
                    print("-----+", end='')
            print()

        else:
        # Caso em que a lista atual é menor que a lista original
            num_espacos = 0
            while (lista[0] != lista_copia[num_espacos]):
                num_espacos += 1
                
            
            
            # Caso em que não há espaços
            if (num_espacos == 0):
                # Primeira linha da moldura
                print("+", end='')
                for i in range(len(lista)):
                    if (i == i_central):
                        print("=====+", end='')
                    else:
                        print("-----+", end='')
                print()

                # Linha central
                print("|", end='')
                for i in range(len(lista)):
                    if (i == i_central):
                        print("|", end='')
                        print(str(lista[i]).zfill(3), end='')
                        print("||", end='')
                    else:
                        print(" ", end='')
                        print(str(lista[i]).zfill(3), end='')
                        print(" |", end='')
                print()

                # Ultima linha da moldura
                print("+", end='')
                for i in range(len(lista)):
                    if (i == i_central):
                        print("=====+", end='')
                    else:
                        print("-----+", end='')
                print()
            else:
            # Caso em que há espaços
                # Primeira linha da moldura
                print(" " * num_espacos * 6, end='')
                print("+", end='')
                for i in range(len(lista)):
                    if (i == i_central):
                        print("=====+", end='')
                    else:
                        print("-----+", end='')
                print()

                # Linha central
                print(" " * num_espacos * 6, end='')
                print("|", end='')
                for i in range(len(lista)):
                    if (i == i_central):
                        print("|", end='')
                        print(str(lista[i]).zfill(3), end='')
                        print("||", end='')
                    else:
                        print(" ", end='')
                        print(str(lista[i]).zfill(3), end='')
                        print(" |", end='')
                print()

                # Ultima linha da moldura
                print(" " * num_espacos * 6, end='')
                print("+", end='')
                for i in range(len(lista)):
                    if (i == i_central):
                        print("=====+", end='')
                    else:
                        print("-----+", end='')
                print()
    else:
        # Primeira linha da moldura
        print("+", end='')
        print("-----+" * len(lista))

        # Linha central
        print("|", end='')
        for i in range(len(lista)):
            print(" ", end='')
            print(str(lista[i]).zfill(3), end='')
            print(" |", end='')
        print()

        # Ultima linha da moldura
        print("+", end='')
        print("-----+" * len(lista))
        



# Input #
procurado = int(input())
lista = input().split()

# Lista de inteiros #
lista_inteiros = []
for x in lista:
    aux = int(x)
    lista_inteiros.append(aux)

tamanho_original = len(lista_inteiros)

lista_ordenada = sorted(lista_inteiros)

lista_copia = lista_inteiros.copy()

print("Elemento procurado:", str(procurado).zfill(3))

lista_moldurada(lista_inteiros, False, lista_copia)

if (lista_inteiros != lista_ordenada):
    print("Lista nao ordenada")
else:
    encontrado = -1
    while (encontrado == -1):
        lista_moldurada(lista_inteiros, True, lista_copia)
        i_central = get_central(lista_inteiros)
        lista_inteiros, encontrado = busca_binaria(lista_inteiros, i_central, procurado)
        if (encontrado != -1):
            for x in range(len(lista_copia)):
                if (lista_copia[x] == encontrado):  
                    print("Encontrado na posicao:", x)
                    break
        else:
            if not lista_inteiros:
                print("O elemento nao foi encontrado")
                break
