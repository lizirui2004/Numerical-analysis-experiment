import numpy as np


def gaussian_elimination_seq(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

    # 消元过程
    for i in range(n):
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            A[j, i:] = A[j, i:] - factor * A[i, i:]
            b[j] = b[j] - factor * b[i]

    # 回代求解
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    return x



def gaussian_elimination_partial_pivoting(A, b):
    A = A.astype(float)
    b = b.astype(float)
    n = len(b)

    # 消元带部分主元
    for i in range(n):
        # 选取主元（当前列最大值）
        max_row = np.argmax(abs(A[i:, i])) + i
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            A[j, i:] = A[j, i:] - factor * A[i, i:]
            b[j] = b[j] - factor * b[i]

    # 回代求解
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
    
    return x
