soma_total = 0

while True:
    # Entrada de dados
    m = int(input("Digite o valor de m (positivo): "))
    n = int(input("Digite o valor de n (positivo e maior ou igual a m): "))

    if m >= n:
        print("Programa encerrado. M deve ser menor que N.")
        break

    soma_parcial = sum(range(m, n + 1))
    soma_total += soma_parcial

    
    print(f"Soma dos números entre {m} e {n} (inclusive): {soma_parcial}")


print(f"Soma total de todos os pares: {soma_total}")
