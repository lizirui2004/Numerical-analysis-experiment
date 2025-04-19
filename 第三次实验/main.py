import numpy as np
import method as m
import time

matrix_path = "target_matrix.npy"
Augmented = np.load(matrix_path)
Coefficient = Augmented[:, :-1]
Constant = Augmented[:, -1]

# 使用 time.perf_counter() 提供更高精度的时间
start = time.perf_counter()
slt_g_s = m.gauss_seidel(Coefficient, Constant, tol=1e-10, max_iter=1000)
end = time.perf_counter()
print("高斯-赛德尔法运行时间:", end - start)
print("高斯-赛德尔法解:", slt_g_s[0])
print("高斯-赛德尔法迭代次数:", slt_g_s[1])

start = time.perf_counter()
slt_jacobi = m.jacobi(Coefficient, Constant, tol=1e-10, max_iter=1000)
end = time.perf_counter()
print("雅可比法运行时间:", end - start)
print("雅可比法解:", slt_jacobi[0])
print("雅可比法迭代次数:", slt_jacobi[1])

start = time.perf_counter()
slt_sor = m.sor(Coefficient, Constant, omega=0.3, tol=1e-6, max_iter=1000)
end = time.perf_counter()
print("SOR法运行时间:", end - start)
print("SOR法解:", slt_sor[0])
print("SOR法迭代次数:", slt_sor[1])

# 使用 np.linalg.solve 直接求解
start = time.perf_counter()
X = np.linalg.solve(Coefficient, Constant)
end = time.perf_counter()
print(f"解 X: {X}")
print(f"np.linalg.solve运行时间: {end - start}")
