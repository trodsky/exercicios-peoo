total_jogadores = 5 * 11
idade_inferior_18 = 0
media_idades_times = [0] * 5
media_alturas = 0
jogadores_mais_80kg = 0

for time in range(5):
    print(f"Time {time + 1}:")
    for jogador in range(11):
        idade = int(input("Digite a idade do jogador: "))
        peso = float(input("Digite o peso do jogador: "))
        altura = float(input("Digite a altura do jogador: "))

        if idade < 18:
            idade_inferior_18 += 1

        media_idades_times[time] += idade
        media_alturas += altura

        if peso > 80:
            jogadores_mais_80kg += 1

media_alturas /= total_jogadores
for time in range(5):
    media_idades_times[time] /= 11

print("Quantidade de jogadores com idade inferior a 18 anos:", idade_inferior_18)
print("Média das idades dos jogadores de cada time:", media_idades_times)
print("Média das alturas de todos os jogadores do campeonato:", media_alturas)
print("Porcentagem de jogadores com mais de 80kg:", (jogadores_mais_80kg / total_jogadores) * 100)
