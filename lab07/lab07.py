objeto_tipo = input()
caracter = input()
dimensao = int(input())

if (objeto_tipo == 'T'):
    if (dimensao < 3):
        print("Dimensao invalida.")
    else:
        j = dimensao - 1
        for i in range (0, dimensao):
            print(j * ' ', end='')
            j -= 1

            print((2*i + 1) * caracter)
            

elif (objeto_tipo == 'Q'):
    if (dimensao < 3):
        print("Dimensao invalida.")
    else:
        for i in range (0, dimensao):
            print(dimensao * caracter)

elif (objeto_tipo == 'L'):
    if (dimensao < 3):
        print("Dimensao invalida.")
    else:
        j = dimensao - 1
        for i in range (0, dimensao):
            print(j * ' ', end='')
            j -= 1

            print((2*i + 1) * caracter)
            
        
        j = 1
        for i in range ((dimensao - 1), 0, -1):
            print(j * ' ', end='')
            j += 1

            print((2*i - 1) * caracter)
            

elif (objeto_tipo == 'H'):
    if (dimensao < 3):
        print("Dimensao invalida.")
    else:
        j = dimensao - 1
        for i in range (0, dimensao):
            print(j * ' ', end='')
            j -= 1

            print((dimensao + i*2) * caracter)
            

        j = 1
        for i in range (1, dimensao):
            print(j * ' ', end='')
            j += 1

            print(((3 * dimensao - 2) - i*2) * caracter)
            
elif (objeto_tipo == 'O'):
    if (dimensao < 3):
        print("Dimensao invalida.")
    else:
        j = dimensao - 1
        for i in range (0, dimensao - 1):
            print(j * ' ', end='')
            j -= 1

            print((dimensao + i*2) * caracter)

        for i in range (0, dimensao):
            print((dimensao + (dimensao - 1)*2) * caracter)

        j = 1
        for i in range (1, dimensao):
            print(j * ' ', end='')
            j += 1

            print(((3 * dimensao - 2) - i*2) * caracter)

else:
    print("Identificador invalido.")