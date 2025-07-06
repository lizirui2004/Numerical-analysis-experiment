import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

colors = [
    'blue',       # 蓝色
    'green',      # 绿色
    'red',        # 红色
    'cyan',       # 青色
    'magenta',    # 洋红
    'yellow',     # 黄色
    'black',      # 黑色
    'orange',     # 橙色
    'purple',     # 紫色
    'brown'       # 棕色
]

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
x_r=np.linspace(-6.28,6.28,100)
y_r=np.cos(x_r)

# 从x中找n个点做拉格朗日插值
for i in range(2,10):
    x = np.linspace(-6.28,6.28,i)
    y = np.cos(x)
    y_approx = lagrange_interp(x, y,x_r )
    plt.plot(x_r, y_approx,linestyle='--',color=colors[i], label=f"拉格朗日插值 {i-1}次")
plt.plot(x_r, y_r, 'black', label="原始数据")
plt.grid()
plt.legend()
plt.title("Lagrange Interpolation rong")
plt.show()