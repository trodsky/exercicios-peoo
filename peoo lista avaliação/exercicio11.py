
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um número inteiro maior que 1: "))

if eh_primo(numero):
    print("Número primo!")
else:
    print("Número não primo.")