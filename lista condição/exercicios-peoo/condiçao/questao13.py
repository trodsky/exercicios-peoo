# Entrada do usuário
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))


bissexto = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)


dias_mes = [31, 28 + bissexto, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


if mes < 1 or mes > 12:
    print("Data inválida!")
else:
    
    if dia < 1 or dia > dias_mes[mes - 1]:
        print("Data inválida!")
    else:
        print("Data válida!")
