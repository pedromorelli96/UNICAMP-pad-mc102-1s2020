entrada = input().split()

lista_palavras = []
lista_numeros = []
lista_hashtags = []
lista_emoticons = []

## Testes ##
for x in entrada:
    if (x[0] == '#'):
        if (x[1:].isalpha()):
            # caso hashtag
            lista_hashtags.append(x)
        else:
            # caso emote
            lista_emoticons.append(x)

    elif (x[0] == '-'):
        if (x[1:].isdigit()):
            # caso numero negativo
            lista_numeros.append(x)
        else:
            # caso emoticon
            lista_emoticons.append(x)

    elif (x.isdigit()):
        # caso numero positivo
        lista_numeros.append(x)
        
    elif (x.isalpha()):
        # caso palavra
        lista_palavras.append(x)

    else:
        # caso emote
        lista_emoticons.append(x)

## Saidas ##
if not lista_palavras:
    print("Palavra(s):")
else:
    print("Palavra(s):", end=' ')
for i in range(len(lista_palavras)):
    if (i != len(lista_palavras)-1):
        # print com espaços
        print(lista_palavras[i], end=' ')
    else:
        # print com newline
        print(lista_palavras[i])

if not lista_numeros:
    print("Numero(s):")
else:
    print("Numero(s):", end=' ')
for i in range(len(lista_numeros)):
    if (i != len(lista_numeros)-1):
        # print com espaços
        print(lista_numeros[i], end=' ')
    else:
        # print com newline
        print(lista_numeros[i])

if not lista_hashtags:
    print("Hashtag(s):")
else:
    print("Hashtag(s):", end=' ')
for i in range(len(lista_hashtags)):
    if (i != len(lista_hashtags)-1):
        # print com espaços
        print(lista_hashtags[i], end=' ')
    else:
        # print com newline
        print(lista_hashtags[i])

if not lista_emoticons:
    print("Emoticon(s):")
else:
    print("Emoticon(s):", end=' ')
for i in range(len(lista_emoticons)):
    if (i != len(lista_emoticons)-1):
        # print com espaços
        print(lista_emoticons[i], end=' ')
    else:
        # print com newline
        print(lista_emoticons[i])
