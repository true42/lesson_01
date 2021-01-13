sec_user = int(input("Введите время в секундах: "))
hour = sec_user//3600
min = sec_user//60 - hour*60

print(f'{hour}:{min}:{sec_user%60}')