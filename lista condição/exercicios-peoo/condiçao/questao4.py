altura = float(input("Qual é a sua altura em metros? "))
sexo = input("Qual é o seu sexo? (Digite 'M' para masculino ou 'F' para feminino): ")

if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
    print("Seu peso ideal é:", peso_ideal)

elif sexo.upper() == "F":
    peso_ideal = (62.1 * altura) - 44.7
    print("Seu peso ideal é:", peso_ideal)

else:
    print("Opção inválida. Por favor, digite 'M' para masculino ou 'F' para feminino.")
