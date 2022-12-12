x=float(input('Введите координаты X: '))
y=float(input('Введите координаты Y: '))
if x>0 and y>0:
    print('1 четверть')
if x<0 and y>0:
    print('2 четверть')  
if x<0 and y<0:
    print('3 четверть')
if x>0 and y<0:
    print('4 четверть')
elif x==0 or y==0:
    print('Введены не корректные данные')
        