salario_carlos = float(input("Digite o salário de Carlos: "))

salario_joao = salario_carlos / 3

rendimento_carlos = 0.02  
rendimento_joao = 0.05    


meses = 0


while salario_joao < salario_carlos:
    salario_carlos += salario_carlos * rendimento_carlos
    salario_joao += salario_joao * rendimento_joao
    meses += 1


print(f"Quantidade de meses necessários: {meses}")
