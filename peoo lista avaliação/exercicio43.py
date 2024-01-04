idades = []
sexos = []
salarios = []

while True:
    idade = int(input("Digite a idade (ou negativo para encerrar): "))
    if idade < 0:
        break

    sexo = input("Digite o sexo ")
    salario = float(input("Digite o salário: "))

    idades.append(idade)
    sexos.append(sexo)
    salarios.append(salario)

media_salarios = sum(salarios) / len(salarios) if len(salarios) > 0 else 0
print("Média dos salários:", media_salarios)

maior_idade = max(idades)
menor_idade = min(idades)
print("Maior idade:", maior_idade)
print("Menor idade:", menor_idade)

mulheres_salario_ate_200 = sum(1 for i in range(len(sexos)) if sexos[i] == 'F' and salarios[i] <= 200)
print("Mulheres com salário até R$ 200", mulheres_salario_ate_200)

indice_menor_salario = salarios.index(min(salarios))
print("Pessoa com menor salário: Idade =", idades[indice_menor_salario], ", Sexo =", sexos[indice_menor_salario])
