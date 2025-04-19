import scipy 
import numpy as np
import math

def func(x,n=0):
    # 定义被积函数
    return x**(2*n+1)*math.exp(-x**2)


def calculate_Integral(f=func,offline=0,online=1):
    # 计算积分
    result, error = scipy.integrate.quad(f, offline, online)
    return result,error


def forward_iteration(k=15,I=calculate_Integral()[0]):
    # 使用递推公式计算 I_{2n}
    results = []
    results.append(I)
    for n in range(1, k+1):
        I = -0.5 * (math.exp(-1) - 2 * n * I)
        results.append(I) 
    return results

if __name__ == "__main__":
    I30=calculate_Integral()
    print(I30)
    print(forward_iteration())

    
