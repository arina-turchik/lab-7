def x(n):
    result = 0
    for i in range(n):
        result = (3 + result) ** 0.5
    return result

print('Введите количество корней(целое число, больше или равно нулю):')
t = int(input())
print("Результат работы функции:", x(t))
