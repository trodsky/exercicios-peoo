preco_ingresso = 5.5

while preco_ingresso >= 1.0:
    qtd_ingressos = 120 + (preco_ingresso - 5.0) / 0.5 * 26
    receita = qtd_ingressos * preco_ingresso
    despesas = 200
    lucro = receita - despesas

    print(f"Preço do ingresso: R$ {preco_ingresso:.2f}")
    print(f"Quantidade de ingressos vendidos: {int(qtd_ingressos)}")
    print(f"Lucro esperado: R$ {lucro:.2f}\n")

    preco_ingresso -= 0.5
