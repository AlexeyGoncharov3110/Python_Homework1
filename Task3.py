quarter_number=int(input('введите номер четверти от 1 до 4 : '))
if quarter_number==1:
    print('x = от 0 до бесконечности, у = от 0 до бесконечности')
if quarter_number==2:
    print('x = от минус бесконечности до 0, у = от 0 до бесконечности')
if quarter_number==3:
    print('x = от минус бесконечности до 0, у = от минус бесконечности до 0')
if quarter_number==4:
    print('x = от 0 до бесконечности, у = от минус бесконечности до 0')
elif quarter_number<1 or quarter_number>4:
    print('Введенны не корректные данные')