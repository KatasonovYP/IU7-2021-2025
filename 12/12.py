"""
Программа, которая по введенным целочисленным
координатам трех точек на плоскости вычисляет стороны
образованного треугольника и длину медианы, проведенной из
наибольшего угла.
Определят, является ли треугольник остроугольным.
Далее вводятся координаты точки. Определяет , находится ли
точка внутри треугольника. Если да, то находит расстояние от точки
до наиболее удаленной стороны треугольника или ее
продолжения.

Катасонов Юрий
ИУ7-15Б
"""


# Вводим координаты x  y в кортежи точек
a = tuple(map(int, input('Enter x and y of point A: ').split()))
b = tuple(map(int, input('Enter x and y of point B: ').split()))
c = tuple(map(int, input('Enter x and y of point C: ').split()))
m = tuple(map(int, input('Enter x and y of point M: ').split()))

# Считаем длины сторон
ab = ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5
ac = ((a[0] - c[0])**2 + (a[1] - c[1])**2)**0.5
bc = ((b[0] - c[0])**2 + (b[1] - c[1])**2)**0.5

# Проверяем треугольник на существование
if ab >= ac + bc or ac >= ab + bc or bc >= ab + ac:
    print('This is not a triangle')
    exit()

# Сортируем стороны по возрастанию
max_side, med_side, min_side = ab, ac, bc
if max_side < med_side: max_side, med_side = med_side, max_side
if max_side < min_side: max_side, min_side = min_side, max_side
if med_side < min_side: med_side, min_side = min_side, med_side

# Считаем медиану
median = (2 * bc**2 + 2 * ac**2 - ab**2)**0.5 / 2

# Считаем длинны векторов к точке P
am = ((a[0] - m[0])**2 + (a[1] - m[1])**2)**0.5
bm = ((b[0] - m[0])**2 + (b[1] - m[1])**2)**0.5
cm = ((c[0] - m[0])**2 + (c[1] - m[1])**2)**0.5

# Считаем полупериметры
p_abc = (ab + ac + bc) / 2
p_abm = (ab + am + bm) / 2
p_acm = (am + ac + cm) / 2
p_bcm = (bm + cm + bc) / 2

# Считаем площади треугольников
s_abc = abs(p_abc * (p_abc - bc) * (p_abc - ac) * (p_abc - ab)) ** 0.5
s_abm = abs(p_abm * (p_abm - bm) * (p_abm - am) * (p_abm - ab)) ** 0.5
s_acm = abs(p_acm * (p_acm - cm) * (p_acm - ac) * (p_acm - am)) ** 0.5
s_bcm = abs(p_bcm * (p_bcm - bc) * (p_bcm - cm) * (p_bcm - bm)) ** 0.5

# Выводим результаты
print(f'\nside AB = {ab:.3f}\nSide AC = {ac:.3f}\nSide BC = {bc:.3f}\n')
print(f'median from greater angle = {median:.3f}\n')
if round(max_side ** 2 - (med_side ** 2 + min_side ** 2), 3) < 0:
    print('acute-angled triangle\n')
else:
    print('triangle not acute-angled\n')
if  -1e-7 < s_abc - (s_abm + s_acm + s_bcm) < 1e-7:
    print('The point lies in the triangle')
    h = max(s_abm / ab, s_acm / ac, s_bcm / bc)  * 2
    print(f'Shortest distance to longest side = {h:.3f}')
else: 
    print('The Point does not lie in a triangle')