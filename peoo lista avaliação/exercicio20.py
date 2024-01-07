total_salarios_masculino = 0
total_salarios_feminino = 0
contador_masculino = 0
contador_feminino = 0

while True:
    
    codigo = int(input("Digite o código do professor (ou 99999 para encerrar): "))

    
    if codigo == 99999:
        print("Programa encerrado.")
        break

    sexo = input("Digite o sexo do professor (M/F): ").upper()
    horas_aula = int(input("Digite o número de horas/aula dadas mensalmente: "))

    
    valor_hora_aula = 30.00
    salario_bruto = horas_aula * valor_hora_aula

    
    if sexo == 'M':
        desconto = 0.10
        contador_masculino += 1
    elif sexo == 'F':
        desconto = 0.05
        contador_feminino += 1
    else:
        print("Sexo inválido. Tente novamente.")
        continue

    salario_liquido = salario_bruto - (salario_bruto * desconto)

    
    print(f"\nCódigo do professor: {codigo}")
    print(f"Salário bruto: R$ {salario_bruto:.2f}")
    print(f"Salário líquido: R$ {salario_liquido:.2f}")

    
    if sexo == 'M':
        total_salarios_masculino += salario_liquido
    elif sexo == 'F':
        total_salarios_feminino += salario_liquido


media_salarios_masculino = total_salarios_masculino / contador_masculino if contador_masculino > 0 else 0
media_salarios_feminino = total_salarios_feminino / contador_feminino if contador_feminino > 0 else 0

print(f"\nMédia dos salários líquidos dos professores do sexo masculino: R$ {media_salarios_masculino:.2f}")
print(f"Média dos salários líquidos dos professores do sexo feminino: R$ {media_salarios_feminino:.2f}")
