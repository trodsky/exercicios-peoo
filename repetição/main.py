quandF = 0
quandM = 0
idadeM = 0 
idade =  0
for i in range(1, 7):
    idade = int(input('idade do participante: '))
    sexo = str(input('sexo: '))
    exp =  str(input('voce tem experiencia na area? :'))

    if sexo == 'M':
        quandM = quandM + 1
        if exp == 'S':
            idadeM = idadeM + idade / 6
            
        elif idade > 45:
            idade45 =  idade45 + 1
            porce = (quandM / idade45) * 100
    else :
        quandF = quandF + 1
        if exp == 'S' :
            if idade < 21 :
                expF = expF + 1
        menor = idade 
        
print('quantidade de mulheres', quandF)
print('quantidade de homens', quandM)
print('idade media dos homens que tem esperiencia : ', idadeM)
print('porcentegem dos homens com mais de 45 :', porce)
print('numero de mulheres que tem menos de 21 anos e tem experiencia : ', expF)
print('menor idade entre as mulheres', menor)