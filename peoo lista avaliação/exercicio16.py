# Entrada de dados
while True:
    try:
        base = float(input())
        altura = float(input())

        
        if base > 0 and altura > 0:
        
            area = (base * altura) / 2
            print(area)
            break
        else:
            print()
    except ValueError:
        print()
