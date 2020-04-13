tempos = []

while (True):
    segundos = int(input())
    if (segundos != -1):
        tempos.append(segundos)
    else:
        break

caracois_0, caracois_1, caracois_2 = (0, 0, 0)
tempo_medio = 0

tempo_em_min = tempos[0]/60
vel = 33/tempo_em_min

vel_min = vel
vel_max = vel

for x in tempos:
    if x < 180:
        caracois_0 += 1
    elif x >= 180 and x < 240:
        caracois_1 += 1
    else:
        caracois_2 += 1

    tempo_medio += x

    tempo_em_min = x/60
    vel = 33/tempo_em_min

    if vel > vel_max:
        vel_max = vel

    if vel < vel_min:
        vel_min = vel


tempo_medio = tempo_medio/(len(tempos))

print("Caracois no nivel 0:", caracois_0)
print("Caracois no nivel 1:", caracois_1)
print("Caracois no nivel 2:", caracois_2)
print("Tempo medio:", format(tempo_medio, '.1f'), "s")
print("Velocidade maxima:", format(vel_max, '.1f'), "cm/min")
print("Velocidade minima:", format(vel_min, '.1f'), "cm/min")
