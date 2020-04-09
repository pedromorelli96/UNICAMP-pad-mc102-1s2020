fatura = float(input())
dias_atraso = int(input())

multa = fatura*(2/100)
juros = (fatura*((0.033)/100))*dias_atraso
valor_total = fatura + multa + juros
renegociacao = valor_total*(10/100)

print("Valor: R$", format(fatura, '.2f'))
print("Multa: R$", format(multa, '.2f'))
print("Juros: R$", format(juros, '.2f'))
print("Valor total: R$", format(valor_total, '.2f'))
print("Valor minimo para renegociacao: R$", format(renegociacao, '.2f'))

