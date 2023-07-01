mes = int(input("Digite o número do mês: "))

if mes == 1:
    signo = "Capricórnio"
elif mes == 2:
    signo = "Aquário"
elif mes == 3:
    signo = "Peixes"
elif mes == 4:
    signo = "Áries"
elif mes == 5:
    signo = "Touro"
elif mes == 6:
    signo = "Gêmeos"
elif mes == 7:
    signo = "Câncer"
elif mes == 8:
    signo = "Leão"
elif mes == 9:
    signo = "Virgem"
elif mes == 10:
    signo = "Libra"
elif mes == 11:
    signo = "Escorpião"
elif mes == 12:
    signo = "Sagitário"
else:
    signo = "Mês inválido"

print("O signo correspondente ao mês é:", signo)
