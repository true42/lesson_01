proceeds, costs = int(input("Введите сумму выручки вашей компании: ")), int(input("Введите сумму издержек вашей компании: "))

if proceeds > costs:
    print(f'Ваша прибыль составила - {proceeds - costs}. Рентабельность выручки - {round((proceeds-costs)/proceeds, 2)}.')
    staff = int(input("Введите, пожалуйста, количество ваших работников: "))
    print(f'Прибыль фирмы в расчёте на одного сотрубника - {(proceeds-costs)/staff}')
elif proceeds == costs:
    print('Вы закрыли издержки.')
else:
    print("Вы работаете в убыток.")