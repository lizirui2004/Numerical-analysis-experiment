import torch
import scipy
import math


def calculate_Integral(n=15,offline=0,online=1):
    # 计算积分
    results=[]
    for i in range(0,n+1):
        f=lambda x,n=i: x**(2*n+1)*math.exp(-x**2)
        result, error = scipy.integrate.quad(f, offline, online)
        results.append(result)
    return results

if __name__ == "__main__":
    pass