def intersect(Z, X):
    if not Z or not X:
        return []
    if Z[0] in X:
        return [Z[0]] + intersect(Z[1:], X)
    else:
        return intersect(Z[1:], X)

A = [1, 2, 3, 4]
B = [3, 4, 5, 6]
result = intersect(A, B)
print(A, B, result)
