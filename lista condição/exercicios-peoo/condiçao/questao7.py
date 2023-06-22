codigo = int(input('codigo do produto: '))

if codigo == 1:
    print('alimento nao perecivel')


elif codigo == 2 or codigo == 3 or codigo ==  4:
    print('alimento perecivel')

elif codigo == 5 or codigo == 6:
    print('vestuario')

elif codigo == 7:
    print('higiene pessoal')

elif codigo < 8 or codigo <= 15:
    print('limpeza')

else :
    print('invalido')