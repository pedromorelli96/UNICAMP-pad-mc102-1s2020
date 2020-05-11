def tupla_float_int(x) :
    x = x[1:-1]       # remove parenteses
    x = x.split(",")  # separa em duas strings
    f = float(x[0])   # converte primeiro elemento para float
    i = int(x[1])     # converte segundo elemento para int
    return (f,i)      # retorna tupla


## Input ##
notas_lab = [tupla_float_int(x) for x in input().split()]

prova1, prova2 = [float(x) for x in input().split()]

## Calculo ##
sum_labs = 0
sum_pesos = 0
for x in notas_lab:
    sum_labs += x[0]*x[1]
    sum_pesos += x[1]
    media_labs = sum_labs/sum_pesos

media_provas = (3*prova1 + 4*prova2)/7

if (media_provas >= 5 and media_labs >= 5):
    exame = False
    media_final = (media_provas*7 + media_labs*3)/10
    aprovado = True
elif (media_provas >= 2.5 and media_labs >= 2.5):
    exame = True
    # Precisa ler a nota do exame
    nota_exame = float(input())
    media_prelim = min(4.9, ((media_provas*7 + media_labs*3)/10))
    media_final = (media_prelim + nota_exame)/2
    if (media_final >= 5):
        aprovado = True
    else:
        aprovado = False
else:
    exame = False
    aprovado = False
    media_final = min(media_labs, media_provas)

## Output ##
print("Media das tarefas de laboratorio:", format(media_labs, '.1f'))
print("Media das provas:", format(media_provas, '.1f'))

if (exame):
    print("Media preliminar:", format(media_prelim, '.1f'))
    print("Nota no exame:", format(nota_exame, '.1f'))

if (aprovado):
    print("Aprovado(a) por nota e frequencia")
else:
    print("Reprovado(a) por nota")

print("Media final:", format(media_final, '.1f'))