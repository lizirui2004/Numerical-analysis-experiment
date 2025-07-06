def newton_interpolation(x, y, x_eval):
    n = len(x)
    # 计算差商表
    F = [[0]*n for _ in range(n)]
    for i in range(n):
        F[i][0] = y[i]
    
    for j in range(1,n):
        for i in range(n-j):
            F[i][j] = (F[i+1][j-1]-F[i][j-1])/(x[i+j]-x[i])
    
    # 计算插值结果
    result = F[0][0]
    for j in range(1,n):
        term = F[0][j]
        for k in range(j):
            term *= (x_eval - x[k])
        result += term
    return result

# 数据
x_data = [3.0, 4.5, 5.0, 7.0, 8.0]
y_data = [9.1, 6.0, -1.2, 3.5, 0]

# 三次插值（使用后4个点）
x_sub = x_data[1:]
y_sub = y_data[1:]
P3 = newton_interpolation(x_sub, y_sub, 5.5)
print(f"三次牛顿插值结果: {P3:.4f}")

# 四次插值（使用全部5个点）
P4 = newton_interpolation(x_data, y_data, 5.5)
print(f"四次牛顿插值结果: {P4:.4f}")