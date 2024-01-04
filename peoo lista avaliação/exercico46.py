votos_candidatos = [0, 0, 0, 0]
votos_nulos = 0
votos_branco = 0
total_votos = 0

while True:
    voto = int(input("Digite o código do candidato: "))

    if voto == 0:
        break
    elif 1 <= voto <= 4:
        votos_candidatos[voto - 1] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_branco += 1
    else:
        print("Código inválido.")

    total_votos += 1

for i in range(4):
    print(f"Total de votos para o candidato {i + 1}: {votos_candidatos[i]}")

print(f"Total de votos nulos: {votos_nulos}")
print(f"Total de votos em branco: {votos_branco}")

porcentagem_nulos = (votos_nulos / total_votos) * 100 if total_votos > 0 else 0
porcentagem_branco = (votos_branco / total_votos) * 100 if total_votos > 0 else 0

print(f"Porcentagem de votos nulos sobre o total de votos: {porcentagem_nulos:.2f}%")
print(f"Porcentagem de votos em branco sobre o total de votos: {porcentagem_branco:.2f}%")