fem = 0
masc = 0
idade_media_homens_exp = 0
perc_homem_mais_45 = 0
mulheres_menos_21_exp = 0
menor_idade_mulher_exp = float('inf')
total_homens = 0
total_homens_exp = 0

while True:

    idade = int(input("Digite a idade do candidato (ou 0 para encerrar): "))

    
    if idade == 0:
        print("Programa encerrado.")
        break

    sexo = input("Digite o sexo do candidato (M/F): ").upper()
    exp = input("O candidato possui experiência no serviço? (S/N): ").upper()


    if sexo == 'F':
        fem += 1
    elif sexo == 'M':
        masc += 1
        total_homens += 1

        if exp == 'S':
            total_homens_exp += 1
            idade_media_homens_exp += idade

            if idade > 45:
                perc_homem_mais_45 += 1

    elif sexo != 'M' and sexo != 'F':
        print("Sexo inválido. Tente novamente.")
        continue

    if sexo == 'F' and idade < 21 and exp == 'S':
        mulheres_menos_21_exp += 1

        if idade < menor_idade_mulher_exp:
            menor_idade_mulher_exp = idade

if total_homens_exp > 0:
    idade_media_homens_exp /= total_homens_exp
    perc_homem_mais_45 = (perc_homem_mais_45 / total_homens_exp) * 100
else:
    print("Não há homens com experiência.")

print(f"\nCandidatos femininos: {fem}")
print(f"Candidatos masculinos: {masc}")
print(f"Idade média dos homens com experiência: {idade_media_homens_exp:.2f}")
print(f"Porcentagem de homens com mais de 45 anos: {perc_homem_mais_45:.2f}%")
print(f"Mulheres com menos de 21 anos e com experiência: {mulheres_menos_21_exp}")
print(f"Menor idade entre mulheres com experiência: {menor_idade_mulher_exp}")
