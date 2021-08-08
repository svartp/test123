rok = int(input("Podaj Rok: "))

if ((rok % 4) == 0):
    if((rok % 100) ==0):
        if ((rok % 400) == 0):
            print(f'{rok} jest przestępny')
        else:
            print(f'{rok} nie jest przestepny!')
    else:
        print(f'{rok} jest przestepny')
else:
    print(f'{rok} nie jest przestepny')