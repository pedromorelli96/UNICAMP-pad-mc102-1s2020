usuarios = []
nome = input()
while (nome != "--"):
    usuarios.append(nome)
    nome = input()

usuarios.sort()

amizades = {}
pessoas = input().split()
while (pessoas[0] != "--"):
    
    if (pessoas[0] not in amizades):
        amizades[pessoas[0]] = list()
        amizades[pessoas[0]].append(pessoas[1])
    else:
        amizades[pessoas[0]].append(pessoas[1])

    if (pessoas[1] not in amizades):
        amizades[pessoas[1]] = list()
        amizades[pessoas[1]].append(pessoas[0])
    else:
        amizades[pessoas[1]].append(pessoas[0])

    pessoas = input().split()


lista_aux = []
for i in range(len(usuarios)):
    for j in range(i+1, len(usuarios)):
        print(f"{usuarios[i]} {usuarios[j]} :",end='')
        
        if (usuarios[i] in amizades):
            if (usuarios[j] in amizades):
                for x in amizades[usuarios[i]]:
                    for y in amizades[usuarios[j]]:
                        if (x == y):
                            lista_aux.append(x)
        # caso lista nao esteja vazia
        primeiro = True
        if lista_aux:
            print(" ", end='')
            for a in sorted(lista_aux):
                if primeiro:
                    print(a, end="")
                    primeiro = False
                else:
                    print(f", {a}", end="")
            print()
        else:
            print()

        lista_aux.clear()

                    
                    

                  





