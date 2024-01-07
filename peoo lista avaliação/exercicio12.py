total_operarios = 15
salario_minimo = 1045.00
folha_pagamento = 0
total_pecas = 0
total_pecas_homem = 0
total_pecas_mulher = 0
maior_salario = 0
numero_maior_salario = 0

for operario in range(1, total_operarios + 1):
    print(f"\nOperário {operario}:")
    numero = int(input("Digite o número do operário: "))
    pecas_mes = int(input("Digite o número de peças fabricadas no mês: "))
    sexo = input("Digite o sexo do operário (M/F): ").upper()

    if pecas_mes <= 30:
        salario = salario_minimo
    elif 31 <= pecas_mes <= 50:
        salario = salario_minimo + 0.03 * (pecas_mes - 30)
    else:
        salario = salario_minimo + 0.05 * (pecas_mes - 30)

    folha_pagamento += salario
    total_pecas += pecas_mes

    if sexo == 'M':
        total_pecas_homem += pecas_mes
    elif sexo == 'F':
        total_pecas_mulher += pecas_mes

    if salario > maior_salario:
        maior_salario = salario
        numero_maior_salario = numero


media_pecas_homem = total_pecas_homem / (total_operarios // 2)
media_pecas_mulher = total_pecas_mulher / (total_operarios // 2)


print("\nResultados da Fábrica:")
print("Número do operário e seu salário:", numero_maior_salario, "R$", maior_salario)
print("Total da folha de pagamento da fábrica:", folha_pagamento)
print("Número total de peças fabricadas no mês:", total_pecas)
print("Média de peças fabricadas pelos homens:", media_pecas_homem)
print("Média de peças fabricadas pelas mulheres:", media_pecas_mulher)
