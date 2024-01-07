soma = 0
quantidade = 0
media = 0
maior = float('-inf')
menor = float('inf')
soma_pares = 0
quantidade_pares = 0
quantidade_impares = 0


while True:
    
    numero = float(input("Digite um número (ou 30000 para encerrar): "))

    
    if numero == 30000:
        print("Programa encerrado.")
        break

    
    soma += numero
    quantidade += 1
    media = soma / quantidade

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

    
    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1
    else:
        quantidade_impares += 1


print(f"\nSoma dos números: {soma}")
print(f"Quantidade de números: {quantidade}")
print(f"Média dos números: {media:.2f}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")


if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
    print(f"Média dos números pares: {media_pares:.2f}")
else:
    print("Não há números pares.")


porcentagem_impares = (quantidade_impares / quantidade) * 100
print(f"Porcentagem de números ímpares: {porcentagem_impares:.2f}%")
