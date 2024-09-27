# Цикл for
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_primes = False
for i in range(1, len(numbers)):
    for j in range(2, numbers[i]):
        is_primes = (numbers[i] % j == 0)
        if is_primes == True:
            not_primes.append(numbers[i])
            break
    if is_primes == False:
        primes.append(numbers[i])
print(f'Простые числа: \n{primes}\n Не простые числа:\n{not_primes}')
