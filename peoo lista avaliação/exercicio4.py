maior_indice = menor_indice = float('inf')
cidade_maior_indice = cidade_menor_indice = 0
total_veiculos = total_acidentes = total_cidades_menos_2000_veiculos = 0
cidades_menos_2000_veiculos = 0

for cidade in range(1, 6):
    codigo = int(input("Digite o codigo da cidade: "))
    veiculos = int(input("Digite o número de veículos de passio: "))
    acidentes = int(input("Digite o número de acidentes de trânsito com vítimas "))

    indice_acidentes = acidentes / veiculos

    if indice_acidentes > maior_indice:
        maior_indice = indice_acidentes
        cidade_maior_indice = codigo

    if indice_acidentes < menor_indice:
        menor_indice = indice_acidentes
        cidade_menor_indice = codigo

    total_veiculos += veiculos
    total_acidentes += acidentes

    if veiculos < 2000:
        total_cidades_menos_2000_veiculos += 1
        cidades_menos_2000_veiculos += veiculos

media_veiculos = total_veiculos / 5
media_acidentes_menos_2000_veiculos = total_acidentes / total_cidades_menos_2000_veiculos

print("Maior índice de acidentes: Cidade", cidade_maior_indice, "com índice", maior_indice)
print("Menor índice de acidentes: Cidade", cidade_menor_indice, "com índice", menor_indice)
print("Média de veículos nas cinco cidades:", media_veiculos)
print("Média de acidentes nas cidades com menos de 2.000 veículos:", media_acidentes_menos_2000_veiculos)
