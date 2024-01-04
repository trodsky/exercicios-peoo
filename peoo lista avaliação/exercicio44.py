lucros = []
lucro_total = 0
acoes_lucro_superior_1000 = 0
acoes_lucro_inferior_200 = 0

while True:
    tipo_acao = input("Digite o tipo de ação ")
    if tipo_acao == 'F':
        break

    preco_compra = float(input("Digite o preço de compra da ação "))
    preco_venda = float(input("Digite o preço de venda da ação: "))

    lucro = preco_venda - preco_compra
    lucros.append(lucro)
    lucro_total += lucro

    if lucro > 1000:
        acoes_lucro_superior_1000 += 1
    elif lucro < 200:
        acoes_lucro_inferior_200 += 1

print("Lucro total da empresa:", lucro_total)
print("Quantidade de ações com lucro superior a R$ 1.000,00:", acoes_lucro_superior_1000)
print("Quantidade de ações com lucro inferior a R$ 200,00:", acoes_lucro_inferior_200)