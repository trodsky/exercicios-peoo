
nome_pais1 = input("Digite o nome do país 1: ")
ouro_pais1 = int(input("Digite a quantidade de medalhas de ouro do país 1: "))
prata_pais1 = int(input("Digite a quantidade de medalhas de prata do país 1: "))
bronze_pais1 = int(input("Digite a quantidade de medalhas de bronze do país 1: "))


nome_pais2 = input("Digite o nome do país 2: ")
ouro_pais2 = int(input("Digite a quantidade de medalhas de ouro do país 2: "))
prata_pais2 = int(input("Digite a quantidade de medalhas de prata do país 2: "))
bronze_pais2 = int(input("Digite a quantidade de medalhas de bronze do país 2: "))


nome_pais3 = input("Digite o nome do país 3: ")
ouro_pais3 = int(input("Digite a quantidade de medalhas de ouro do país 3: "))
prata_pais3 = int(input("Digite a quantidade de medalhas de prata do país 3: "))
bronze_pais3 = int(input("Digite a quantidade de medalhas de bronze do país 3: "))


pontuacao_pais1 = ouro_pais1 * 3 + prata_pais1 * 2 + bronze_pais1
pontuacao_pais2 = ouro_pais2 * 3 + prata_pais2 * 2 + bronze_pais2
pontuacao_pais3 = ouro_pais3 * 3 + prata_pais3 * 2 + bronze_pais3


print("Classificação Olímpica:")
print("1º lugar:", nome_pais1, "- Pontuação:", pontuacao_pais1)
print("2º lugar:", nome_pais2, "- Pontuação:", pontuacao_pais2)
print("3º lugar:", nome_pais3, "- Pontuação:", pontuacao_pais3)
