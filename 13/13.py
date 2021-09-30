"""


"""

# Импортируем модуль
import math as m

def f(x):
    return x ** 2 - 7

# Создаём переменные
limit_x = (-4, 4)
limit_y = (m.nan, m.nan)
x = limit_x[0]
step = 0.5

# Создадим переменные, для масштабирования графика по оси y
max_plot_hight = 20
hight = 0

# Построим таблицу значений
print(f'\n {"x":^7} {"y":^11} ')
print('|———————|———————————|')
while x <= limit_x[1]:
    y = f(x)
    limit_y = (min(round(y), limit_y[0]), max(round(y), limit_y[1]))
    print(f'|{x:^7.3g}|{y:^11.5g}|')
    print(f'|{"":—^7}|{"":—^11}|')
    x += step

# Построим график функции
for y in range(limit_y[1] + 1, limit_y[0] - 2, -1):
    print(f'\n{y if y % 2 == 0 else "":>5}  ', end='')
    x = limit_x[0] - step
    while x <= limit_x[1] + step:
        sym = ' '
        if x == 0: sym = '|'
        elif y == 0: sym = '—'
        if abs(y - f(x)) <= step: sym = '*'
        print(sym, end='')
        x += step
    
    # Если график по высоте больше, чем нам нужно, то прекращаем строить график
    hight += 1
    if hight > max_plot_hight:
        break