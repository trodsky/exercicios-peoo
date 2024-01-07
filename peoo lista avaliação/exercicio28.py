faixas_etarias = [0, 0, 0, 0, 0]
total_pessoas = 8

for i in range(total_pessoas):
    idade = int(input(f"Digite a idade da pessoa {i + 1}: "))
    
    if idade <= 15:
        faixas_etarias[0] += 1
    elif 16 <= idade <= 30:
        faixas_etarias[1] += 1
    elif 31 <= idade <= 45:
        faixas_etarias[2] += 1
    elif 46 <= idade <= 60:
        faixas_etarias[3] += 1
    else:
        faixas_etarias[4] += 1

porcentagem_primeira_faixa = (faixas_etarias[0] / total_pessoas) * 100
porcentagem_ultima_faixa = (faixas_etarias[4] / total_pessoas) * 100

print(f"\nQuantidade de pessoas em cada faixa etária:")
for i, faixa in enumerate(faixas_etarias, start=1):
    print(f"Faixa {i}: {faixa} pessoas")

print(f"\nPorcentagem de pessoas na primeira faixa etária: {porcentagem_primeira_faixa:.2f}%")
print(f"Porcentagem de pessoas na última faixa etária: {porcentagem_ultima_faixa:.2f}%")
