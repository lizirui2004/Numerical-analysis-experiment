def lagrange_interp(x_data, y_data, x0):
    n = len(x_data)
    result = 0.0
    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if j != i:
                term *= (x0 - x_data[j]) / (x_data[i] - x_data[j])
        result += term
    return result

# 原始数据
x_all = [3.0, 4.5, 5.0, 7.0, 8.0]
y_all = [9.1, 6.0, -1.2, 3.5, 0.0]
x_target = 5.5

# (1) 三次拉格朗日插值（选4个点）：例如选择 4.5, 5.0, 7.0, 8.0
x_3 = x_all[1:]
y_3 = y_all[1:]

# (2) 四次拉格朗日插值（全部5个点）
x_4 = x_all
y_4 = y_all

# 插值结果
y_approx_3 = lagrange_interp(x_3, y_3, x_target)
y_approx_4 = lagrange_interp(x_4, y_4, x_target)

print(f"三次拉格朗日插值在 x=5.5 处的近似值：{y_approx_3:.4f}")
print(f"四次拉格朗日插值在 x=5.5 处的近似值：{y_approx_4:.4f}")
