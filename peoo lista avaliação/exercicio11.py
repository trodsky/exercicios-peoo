numero = int(input("Digite um número inteiro maior que 1: ")) 

if numero > 1:
    primo = True
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break

    if primo:
        print("Número primo!")
    else:
        print("Número não primo.")
else:
    print("Número não primo. Digite um número maior que 1.")
