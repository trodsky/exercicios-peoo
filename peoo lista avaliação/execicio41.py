idades = []
idade = int(input("Digite a idade (ou 0 para encear): "))

while idade != 0:
    idades.append(idade)
    idade = int(input("Digite a idade: "))

media = sum(idades) / len(idades) if len(idades) > 0 else 0
print("A média das idades ", media)
