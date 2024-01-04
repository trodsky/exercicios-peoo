n = int(input("Digite o número de termos N: "))
x = float(input("Digite um valor positivo para X: "))
s = 0
potencia = 2
sinal = -1

for i in range(1, n * 2, 2):
    s += (sinal * x ** potencia) / math.factorial(i)
    potencia += 2
    sinal *= -1

print("O valor da série é:", s)
