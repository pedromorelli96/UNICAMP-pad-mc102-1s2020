# Parte 1: leitura dos inputs
massa = float(input())

idade = int(input())
if (idade == 16 or idade == 17):
    doc_autorizacao = input()

febre_sintomas = input()

viagem_exterior = input()

contato_suspeito = input()

primeira_doacao = input()
if (primeira_doacao == 'N'):
    doacoes_12 = int(input())
    if (doacoes_12 > 0):
        meses_ultima_doacao = int(input())
    

sexo = input()
if (sexo == 'F'):
    gravida = input()

# Parte 2: print dos inputs
print('Massa corporal:', massa)
print('Idade:', idade)
if (idade == 16 or idade == 17):
    print('Documento de autorizacao:', doc_autorizacao)
print('Febre ou sintomas gripais:', febre_sintomas)
print('Viagem recente ao exterior:', viagem_exterior)
print('Contato com caso de COVID-19:', contato_suspeito)
print('Primeira doacao:', primeira_doacao)
if (primeira_doacao == 'N'):
    print('Doacoes nos ultimos 12 meses:', doacoes_12)
    if (doacoes_12 > 0):
        print('Meses desde ultima doacao:', meses_ultima_doacao)
    
print('Sexo biologico:', sexo)
if (sexo == 'F'):
    print('Gravida ou amamentando:', gravida)

# Parte 3: print das impedimentos

# variavel auxiliar
flag_impedimento = 0

if (massa < 50):
    print('Impedimento: abaixo da massa corporal minima')
    flag_impedimento = 1
if (idade < 16):
    print('Impedimento: menor de 16 anos')
    flag_impedimento = 1
if (idade == 16 or idade == 17):
    if (doc_autorizacao == 'N'):
        print('Impedimento: menor de 18 anos sem consentimento dos responsaveis')
        flag_impedimento = 1
if (idade > 69):
    print('Impedimento: maior de 69 anos')
    flag_impedimento = 1
if (idade > 60 and idade < 70):
    if (primeira_doacao == 'S'):
        print('Impedimento: maior de 60 anos e primeira doacao')
        flag_impedimento = 1
if (febre_sintomas == 'S'):
    print('Impedimento: febre ou sintomas gripais')
    flag_impedimento = 1
if (viagem_exterior == 'S'):
    print('Impedimento: viagem recente ao exterior')
    flag_impedimento = 1
if (contato_suspeito == 'S'):
    print('Impedimento: contato com caso de COVID-19')
    flag_impedimento = 1
if (primeira_doacao == 'N'):
    if (sexo == 'M'):
        if (doacoes_12 >= 4):
            print('Impedimento: numero maximo de doacoes anuais foi atingido')
            flag_impedimento = 1
        if (doacoes_12 > 0):
            if (meses_ultima_doacao <= 2):
                print('Impedimento: intervalo minimo entre as doacoes nao foi respeitado')
                flag_impedimento = 1
    if (sexo == 'F'):
        if (doacoes_12 >= 3):
            print('Impedimento: numero maximo de doacoes anuais foi atingido')
            flag_impedimento = 1
        if (doacoes_12 > 0):
            if (meses_ultima_doacao <= 3):
                print('Impedimento: intervalo minimo entre as doacoes nao foi respeitado')
                flag_impedimento = 1
if (sexo == 'F'):
    if (gravida == 'S'):
        print('Impedimento: gravida ou amamentando')
        flag_impedimento = 1

if (flag_impedimento == 0):
    print('Agende um horario para triagem completa')