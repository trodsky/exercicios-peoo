mes = int(input("Digite o número do mês (1 a 12): "))

if mes == 1:
    nome_mes = "Janeiro"
elif mes == 2:
    nome_mes = "Fevereiro"
elif mes == 3:
    nome_mes = "Março"
elif mes == 4:
    nome_mes = "Abril"
elif mes == 5:
    nome_mes = "Maio"
elif mes == 6:
    nome_mes = "Junho"
elif mes == 7:
    nome_mes = "Julho"
elif mes == 8:
    nome_mes = "Agosto"
elif mes == 9:
    nome_mes = "Setembro"
elif mes == 10:
    nome_mes = "Outubro"
elif mes == 11:
    nome_mes = "Novembro"
elif mes == 12:
    nome_mes = "Dezembro"
else:
    nome_mes = "mês inválido, cara"

print(nome_mes)
