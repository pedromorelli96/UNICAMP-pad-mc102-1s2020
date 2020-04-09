tosse_str = input()
febre_str = input()
difresp_str = input()

tosse_bool = tosse_str == 'True'
febre_bool = febre_str == 'True'
difresp_bool = difresp_str == 'True'

print('Tosse:', tosse_bool)
print('Febre:', febre_bool)
print('Dificuldade para respirar:', difresp_bool)

provavelmente_covid = tosse_bool and febre_bool and difresp_bool

print('Provavelmente eh COVID-19:', provavelmente_covid)
