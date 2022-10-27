tickets = int(input("Введите количество билетов: "))
person = tickets
cash = 0
while person != 0:
    age_for_ticket = int(input(f'Для какого возраста приобретается билет № {person} ? '))
    if age_for_ticket < 18:
        print('Вход бесплатный')
    elif 25 > age_for_ticket >= 18:
        cash += 990
        print('Стоимость: 990 руб.')
    else:
        cash += 1390
        print('Стоимость: 1390 руб.')
    person -= 1
if tickets > 3:
    sale = cash - ((cash / 100) * 10)
    print(f'К оплате {sale} руб., применена скидка 10% за покупку более 3 билетов')
else:
    print(f'К оплате {cash} руб.')