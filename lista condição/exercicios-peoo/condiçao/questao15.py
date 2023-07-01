idade = int(input("Digite a idade da pessoa: "))

if idade < 16:
    classe_eleitoral = "Não votante"
elif idade >= 18 and idade <= 65:
    classe_eleitoral = "Eleitor obrigatório"
else:
    classe_eleitoral = "Eleitor facultativo"

print("A classe eleitoral da pessoa é:", classe_eleitoral)
