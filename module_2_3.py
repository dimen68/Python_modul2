# Нули ничто, отрицание недопустимо!
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
new_list = []
l = len(my_list)
l1 = -1
while l > l1:
    l1 +=1
    if my_list[l1] < 0:
        break
    elif my_list[l1] == 0:
        continue
    else:
        print(my_list[l1])
        new_list.append(my_list[l1])
print(f'Список составлен:\n {new_list}')
