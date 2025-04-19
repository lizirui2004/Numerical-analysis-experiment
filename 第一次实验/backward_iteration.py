import scipy 
import numpy as np
import math

def func(x,n=30):
    # 定义被积函数
    return x**(2*n+1)*math.exp(-x**2)

def calculate_Integral(f=func,offline=0,online=1):
    # 计算积分
    result, error = scipy.integrate.quad(f, offline, online)
    return result,error

def backward_iteration(k=15,I15=0.06):
    # 使用递推公式计算 I_{2n}
    results = []
    results.append(I15)
    I_prev = I15
    # 反向递推
    for n in range(k, 0, -1):
        I_prev = math.exp(-1)/(2*n) + I_prev/n
        results.append(I_prev)
    results.reverse()
    return results


if __name__ == "__main__":
    I15=calculate_Integral()
    print(I15)
    print(backward_iteration())