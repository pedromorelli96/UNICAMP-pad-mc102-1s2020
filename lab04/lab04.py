x = float(input())
y = float(input())
z = float(input())

# definição do maior valor

if (x >= y and x >= z):
    a = x
    b = y
    c = z
elif (y >= x and y >= z):
    a = y
    b = x
    c = z
else:
    a = z
    b = x
    c = y

# teste de valores inválidos

if (a == 0 or b == 0 or c == 0):
    print('Valores invalidos na entrada')
    exit()
elif (a < 0 or b < 0 or c < 0):
    print('Valores invalidos na entrada')
    exit()
elif (a >= (b+c) or b >= (a+c) or c >= (a+b)):
    print('Valores invalidos na entrada')
    exit()

# b^2 + c^2
bc_quadrado = b**2 + c**2

# a^2
a_quadrado = a**2

# teste quanto aos lados
if (a == b and b == c):
    print('Triangulo equilatero')
elif (a == b or b == c or a == c):
    print('Triangulo isosceles')
else:
    print('Triangulo escaleno')

# teste quanto aos angulos
if (a_quadrado > bc_quadrado):
    print('Triangulo obtusangulo')
elif (a_quadrado == bc_quadrado):
    print('Triangulo retangulo')
elif (a_quadrado < bc_quadrado):
    print('Triangulo acutangulo')