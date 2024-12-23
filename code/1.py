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