# Лабораторная работа №7
### Вариант №6
## Ход работы:
1. Разобрать работу рекурсий.
2. Написать программы для решения заданий.
3. Загрузить решение на `github`.

### Задача №1
Функция для нахождения пересечения двух списков.
#### Решение:
```
def intersect(Z,X):
    C=[]
    for z in Z:
        for x in X:
            if z==x:
                C.append(z)
                break
    return C

A=[]
B=[]
print('Введите длину списка 1:')
n1=int(input())
print('Введите список 1:')
for i in range(n1):
    a=int(input())
    A.append(a)
print('Введите длину списка 2:')
n2=int(input())
print('Введите список 2:')
for i in range(n2):
    b=int(input())
    B.append(b)
print('Ваши списки:', A, B)
print('Их пересечение:', intersect(A,B))
```
### Задача №2
Функция для расчёта <image src= av.png alt="функция">.
### Решение:
```
def x(n):
    if n==0:
        return 0
    else:
        return (3+x(n-1))**(0.5)

print('Введите количество корней(целое число, больше или равно нулю):')
t=int(input())
print("Результат работы функции:",x(t))
```
## Источники:
[evil-teacher](https://evil-teacher.on-fleek.app/prog_pm/term1/lab07/)
