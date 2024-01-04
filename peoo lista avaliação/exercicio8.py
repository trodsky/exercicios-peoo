
n = int(input("Digite o número de termos: "))

serie = []

for i in range(1, n + 1):
    if i % 2 == 1:
        serie.append(2 ** i)
    else:
        serie.append((i // 2) * 7)

print("Os valores da série são:", serie)
