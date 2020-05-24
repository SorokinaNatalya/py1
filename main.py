a=int(input('введите значение А='))
b=int(input('введите значение Б='))
if a>b:
    print('Свершилось!')
elif b>a:
    print('Да ну !')
else:
    print('А если так ?')
    c = int(input('введите значение В='))
    if (a+c)>(b-c):
          print('Свершилось!')
    elif (b-c)>(a+c):
          print('Да ну !')
