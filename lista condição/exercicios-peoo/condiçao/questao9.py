preco_etiqueta = float(input("Digite o preço normal de etiqueta: "))
condicao_pagamento = int(input("Digite o código da condição de pagamento (1, 2, 3 ou 4): "))

if condicao_pagamento == 1:
    desconto = preco_etiqueta * 0.1
    valor_pago = preco_etiqueta - desconto
elif condicao_pagamento == 2:
    desconto = preco_etiqueta * 0.05
    valor_pago = preco_etiqueta - desconto
elif condicao_pagamento == 3:
    valor_pago = preco_etiqueta / 2
elif condicao_pagamento == 4:
    juros = preco_etiqueta * 0.1
    valor_pago = preco_etiqueta + juros
else:
    print("Condição de pagamento inválida!")

if condicao_pagamento in [1, 2, 3, 4]:
    print("O valor a ser pago é R$", valor_pago)
