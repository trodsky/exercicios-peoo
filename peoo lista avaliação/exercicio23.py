salario_minimo = float(input("Digite o valor do salário mínimo: "))
quilowatt_custo = salario_minimo / 8


total_valor_pagar = 0

while True:

    tipo_consumidor = int(input("Digite o tipo de consumidor (1 - residencial, 2 - comercial, 3 - industrial): "))
    
    
    if tipo_consumidor not in [1, 2, 3]:
        print("Programa encerrado.")
        break
    
    quantidade_quilowatt = float(input("Digite a quantidade de quilowatts consumida: "))

    
    valor_consumo = quantidade_quilowatt * quilowatt_custo

    
    if tipo_consumidor == 1:
        acrescimo = 5
    elif tipo_consumidor == 2:
        acrescimo = 10
    else:
        acrescimo = 15

    valor_pagar = valor_consumo + (valor_consumo * acrescimo / 100)
    total_valor_pagar += valor_pagar

    
    print(f"\nValor de cada quilowatt: R$ {quilowatt_custo:.2f}")
    print(f"Valor a ser pago pelo consumidor: R$ {valor_pagar:.2f}")

print(f"\nTotal a ser pago por todos os consumidores: R$ {total_valor_pagar:.2f}")
