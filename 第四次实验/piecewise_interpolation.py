import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题
# 数据点
x_points = np.array([3.0, 4.5, 5.0, 7.0, 8.0])
y_points = np.array([9.1, 6.0, -1.2, 3.5, 0])

# 为每一段生成插值
x_interp = []
y_interp = []

for i in range(len(x_points) - 1):
    # 在线段之间采样一些点（用于平滑连接）
    x_segment = np.linspace(x_points[i], x_points[i+1], 100)
    y_segment = y_points[i] + (y_points[i+1] - y_points[i]) / (x_points[i+1] - x_points[i]) * (x_segment - x_points[i])
    x_interp.extend(x_segment)
    y_interp.extend(y_segment)

# 绘图
plt.figure(figsize=(8, 5))
plt.plot(x_interp, y_interp, label="分段线性插值", color='blue')
plt.scatter(x_points, y_points, color='red', label="数据点")
plt.title("分段线性插值图像")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
