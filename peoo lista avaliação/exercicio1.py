
salario = 1000.00


aumento_2006 = 0.015
salario *= (1 + aumento_2006)


for ano in range(2007, 2023):
    aumento_anterior = aumento_2006
    aumento_ano_atual = 2 * aumento_anterior
    salario *= (1 + aumento_ano_atual)


print("O salário atual do funcionário é: R$ {:.2f}".format(salario))