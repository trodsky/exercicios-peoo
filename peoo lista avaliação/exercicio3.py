n = int(input("Digite o número de valores inteiros e positivos: "))

for _ in range(n):
    valor = int(input("Digite um valor inteiro e positivo: "))
    fatorial = math.factorial(valor)
    print(f"Valor: {valor}, Fatorial: {fatorial}")


