import numpy as np
import matplotlib.pyplot as plt

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
# 输入数据
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2.8, 5.4, 1.9, 0, 0.6, 1.8, 3.4, 5.0, 5.8])

# 构造设计矩阵（7次多项式有8个系数）
X = np.column_stack([x**i for i in range(8)])

# 最小二乘法求解系数
coefficients = np.linalg.lstsq(X, y, rcond=None)[0]

# 输出结果
print("7次多项式系数（从a0到a7）：")
for i, coef in enumerate(coefficients):
    print(f"a_{i} = {coef:.8f}")

# 构造多项式函数
def poly(x_val, coeffs):
    return sum(coeff * x_val**i for i, coeff in enumerate(coeffs))

# 验证拟合效果
print("\n拟合值与实际值对比：")
for xi, yi in zip(x, y):
    print(f"x={xi}: 实际y={yi:.1f}, 拟合y={poly(xi, coefficients):.2f}")

# 绘制拟合曲线
plt.scatter(x, y, color='red', label='实际数据')
x_fit = np.linspace(0, 8, 100)
y_fit = poly(x_fit, coefficients)
plt.plot(x_fit, y_fit, label='7次多项式拟合')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('7次最小二乘多项式拟合')
plt.grid(True)
plt.show()