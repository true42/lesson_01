user_number = input("Введите положительно число: ")
max_number = 0

while(max_number < 9 and user_number != ""):
    if max_number < int(user_number[-1]):
        max_number = int(user_number[-1])
        user_number = user_number[:-1]
    else:
        user_number = user_number[:-1]

print(max_number)
