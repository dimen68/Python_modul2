# Все ли равны?
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третие число: '))
if first == second == third: # или first == second and second == third
    print('Количество равных чисел - 3')
elif first == second or second == third or first == third:
    print('Количество равных чисел - 2')
else:
    print('Количество равных чисел - 0')