# Слишком древний шифр
result = [0] * 21
for i in range(3,21):
    for j in range(1,i):
        for k in range(j+1,i):
            if i % (j + k) == 0:
                result[i] = int(str(result[i]) + str(j) + str(k))
print('Пароли расчитаны.')
while 3 < 20:
    code = int(input('Введите число указанное на первом поле камня (3-20): '))
    if 2 < code < 21:
        print(f'Пароль для числа {code} - {result[code]}')
    else:
        print(f'Число {code} вне допустимого диапазона.\nБудьте внимательней!')
        break
print('Программа завершена')