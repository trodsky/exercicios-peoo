n = 8

termo1, termo2 = 1, 1

print("Os oito primeiros termos da sequência de Fibonacci:")
for _ in range(n):
    print(termo1, end=" ")
    termo1, termo2 = termo2, termo1 + termo2
