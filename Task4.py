xA=float(input('Введите координаты первой точки XА: '))
yA=float(input('Введите координаты первой точки YА: '))
xB=float(input('Введите координаты второй точки XB: '))
yB=float(input('Введите координаты второй точки YB: '))
import math
dist= math.sqrt ((xA-xB)*(xA-xB) + (yA-yB)*(yA-yB)) 
print(round(dist,3))