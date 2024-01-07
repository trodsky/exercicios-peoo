total_criancas = int(input("Digite o número total de crianças nascidas no período: "))
criancas_feminino_mortas = 0
criancas_masculino_mortas = 0
criancas_24_meses_ou_menos = 0

for crianca in range(1, total_criancas + 1):
    print(f"\nCriança {crianca}:")
    sexo = input("Digite o sexo da criança (M/F): ").upper()
    tempo_vida = int(input("Digite o tempo de vida da criança em meses: "))

    if sexo == 'F' and tempo_vida > 0:
        criancas_feminino_mortas += 1
    elif sexo == 'M' and tempo_vida > 0:
        criancas_masculino_mortas += 1

    if tempo_vida <= 24:
        criancas_24_meses_ou_menos += 1

percentagem_feminino_mortas = (criancas_feminino_mortas / total_criancas) * 100 if total_criancas > 0 else 0
percentagem_masculino_mortas = (criancas_masculino_mortas / total_criancas) * 100 if total_criancas > 0 else 0
percentagem_24_meses_ou_menos = (criancas_24_meses_ou_menos / total_criancas) * 100 if total_criancas > 0 else 0

print("\nResultados da Pesquisa:")
print("Percentagem de crianças do sexo feminino mortas no período:", percentagem_feminino_mortas, "%")
print("Percentagem de crianças do sexo masculino mortas no período:", percentagem_masculino_mortas, "%")
print("Percentagem de crianças que viveram 24 meses ou menos no período:", percentagem_24_meses_ou_menos, "%")
