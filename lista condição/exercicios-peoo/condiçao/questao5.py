ano = int(input('ano de nascimento:: '))

idade = 2023 - ano


if idade > 16:
    print(idade, ' anos.ja pode votar')

if idade > 18:
    print('tambem pode dirigir')

else :
    print('muito jovem')
