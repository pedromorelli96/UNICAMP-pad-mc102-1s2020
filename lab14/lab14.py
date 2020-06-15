def cria_tela(char_preto, altura):
    # Cria matriz de caracteres com char_preto
    tela = [ [char_preto for j in range(altura)] for i in range(altura)]
    return tela

def print_tela_com_moldura(tela, altura):
    # Primeira linha da moldura 
    print("+" + "-"*(altura+2) + "+")
    # Segunda linha da moldura
    print("|" + " "*(altura+2) + "|")

    # Linhas centrais da moldura
    for linha in tela:
        print("| ", end='')
        for elemento in linha:
            print(elemento, end='')
        print(" |")

    # Penultima linha da moldura
    print("|" + " "*(altura+2) + "|")
    # Ultima linha da moldura
    print("+" + "-"*(altura+2) + "+")


def modifica_quadrado(tela, altura, x, y, p):
    if (p == 1):
        novo_x = x + altura//4
        for linha in range(y, y+(altura//2)):
            for elemento in range(x, novo_x):
                tela[linha][elemento] = " "
            for elemento in range((novo_x + altura//2), (novo_x + altura//2) + altura//4):
                tela[linha][elemento] = " "

    else:
        novo_x = x + altura//4
        for linha in range(y, y+(altura//2)):
            for elemento in range(x, novo_x):
                tela[linha][elemento] = " "
            for elemento in range((novo_x + altura//2), (novo_x + altura//2) + altura//4):
                tela[linha][elemento] = " "

        modifica_quadrado(tela, altura//2, x+altura//4, y, p - 1)
        modifica_quadrado(tela, altura//2, x, y+altura//2, p - 1)
        modifica_quadrado(tela, altura//2, x+altura//2, y+altura//2, p - 1)


N = int(input())
p = int(input())
char_preto = input()
altura = 2**N

x = 0
y = 0

tela = cria_tela(char_preto, altura)

if (p == 0):
    print_tela_com_moldura(tela, altura)
else:
    modifica_quadrado(tela, altura, x, y, p)
    print_tela_com_moldura(tela, altura)

