number = int(input("Введите число от 1 до 7: "))    
def weekday(number):
    if 6 <= number <= 7:
        print("ДА")
    elif 0 < number < 6:
        print("НЕТ")
    else:
        print("Введены не корректные данные")   
weekday(number)          