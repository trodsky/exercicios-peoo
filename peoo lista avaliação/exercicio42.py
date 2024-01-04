canais_audiencia = {4: 0, 5: 0, 7: 0, 12: 0}

while True:
    canal = int(input("Digite o número do canal "))
    if canal == 0:
        break
    pessoas_assistindo = int(input("Digite o número de pessoas assistindo: "))
    canais_audiencia[canal] += pessoas_assistindo

total_pessoas = sum(canais_audiencia.values())
for canal, audiencia in canais_audiencia.items():
    porcentagem = (audiencia / total_pessoas) * 100 if total_pessoas > 0 else 0
    print(f"Canal {canal}: {porcentagem:.2f}% de audiência")
