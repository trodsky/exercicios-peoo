while True:
    print("Menu de opções:")
    print("1 – Média aritmética")
    print("2 – Média ponderada")
    print("3 – Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        media_aritmetica = (nota1 + nota2) / 2
        print("Média", media_aritmetica)
    elif opcao == 2:
        nota1 = float(input("Digite a primeira nota: "))
        peso1 = float(input("Digite o peso da primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        peso2 = float(input("Digite o peso da segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
        peso3 = float(input("Digite o peso da terceira nota: "))
        media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
        print("Média ponderada:", media_ponderada)
    elif opcao == 3:
        print("Saindo")
        break
    else:
        print("Opção inválida. ")
