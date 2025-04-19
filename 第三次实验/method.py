import numpy as np



def jacobi(A, b, tol=1e-10, max_iter=1000):
    n = len(b)
    x = np.zeros(n)  # 初始化解向量
    x_new = np.zeros(n)  # 新的解向量用于存储每次迭代的结果
    
    initial_residual = np.linalg.norm(b - np.dot(A, x))  # 初始残差
    for k in range(max_iter):
        for i in range(n):
            # 雅可比法的迭代公式
            x_new[i] = (b[i] - np.dot(A[i, :], x) + A[i, i] * x[i]) / A[i, i]
        
        # 检查收敛性，计算相对误差
        current_residual = np.linalg.norm(b - np.dot(A, x_new))
        if current_residual / initial_residual < tol:
            return x_new, k + 1
        
        x = x_new.copy()
    
    return x_new, max_iter



def gauss_seidel(A, b, tol=1e-10, max_iter=1000):
    n = len(b)
    x = np.zeros(n)  # 初始化解向量
    initial_residual = np.linalg.norm(b - np.dot(A, x))  # 初始残差

    for k in range(max_iter):
        x_new = x.copy()  # 每次迭代前记录当前解
        for i in range(n):
            # 高斯-赛德尔法的迭代公式
            x_new[i] = (b[i] - np.dot(A[i, :], x_new) + A[i, i] * x_new[i]) / A[i, i]
        
        # 检查收敛性，计算相对误差
        current_residual = np.linalg.norm(b - np.dot(A, x_new))
        if current_residual / initial_residual < tol:
            return x_new, k + 1
        
        x = x_new.copy()
    
    return x_new, max_iter




def sor(A, b, omega=1.25, tol=1e-6, max_iter=1000):
    n = len(b)
    x = np.zeros(n)  # 初始化解向量z
    
    # 计算初始残差
    initial_residual = np.linalg.norm(b - np.dot(A, x))
    
    for k in range(max_iter):
        x_new = x.copy()  # 记录当前解
        for i in range(n):
            # SOR迭代公式
            sum1 = np.dot(A[i, :i], x_new[:i])  # 左边的和
            sum2 = np.dot(A[i, i+1:], x[i+1:])  # 右边的和
            x_new[i] = (1 - omega) * x[i] + omega * (b[i] - sum1 - sum2) / A[i, i]
        
        # 计算当前残差
        current_residual = np.linalg.norm(b - np.dot(A, x_new))
        
        # 判断停机条件
        if current_residual / initial_residual < tol:
            return x_new, k + 1
        
        x = x_new.copy()
    
    return x_new, max_iter

