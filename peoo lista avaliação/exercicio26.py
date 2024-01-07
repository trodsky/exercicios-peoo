grupos = []
for i in range(5):
    grupo = []
    for j in range(4):
        valor = float(input(f"Digite o valor {j+1} do grupo {i+1}: "))
        grupo.append(valor)
    grupos.append(grupo)

print("\nGrupos na ordem lida:")
for grupo in grupos:
    print(grupo)

crescente = sorted(grupos, key=lambda x: x[0])
print("\nGrupos em ordem crescente:")
for grupo in crescente:
    print(grupo)

decrescente = sorted(grupos, key=lambda x: x[0], reverse=True)
print("\nGrupos em ordem decrescente:")
for grupo in decrescente:
    print(grupo)
