a, b = int(input("Введи расстояние, которое пробежал спортсмен: ")), int(input("Введи расстояние, которое необходимо пробежать спортсмену: "))
day = 1

while a < b:
    a += a/10
    day += 1

print(f'На {day}-й день спортсмен достиг результата - не менее {b} км.')