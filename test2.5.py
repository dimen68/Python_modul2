def get_matrix(n, m, value):
    row_ = ([value] * m)
    matrix =([row_]*n)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
for i in result1:
    print(i)
for j in result2:
    print(j)
for k in result3:
    print(k)

