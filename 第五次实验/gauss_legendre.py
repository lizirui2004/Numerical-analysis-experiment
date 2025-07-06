import numpy as np

def gauss_legendre_3(f, a, b):
    # 三点高斯-勒让德求积
    t = np.array([-np.sqrt(3/5), 0, np.sqrt(3/5)])
    w = np.array([5/9, 8/9, 5/9])
    x = (b - a)/2 * t + (a + b)/2
    return (b - a)/2 * np.sum(w * f(x))

def gauss_legendre_5(f, a, b):
    # 五点高斯-勒让德求积
    t = np.array([
        -np.sqrt((5 + 2*np.sqrt(10/7))/3),
        -np.sqrt((5 - 2*np.sqrt(10/7))/3),
        0,
        np.sqrt((5 - 2*np.sqrt(10/7))/3),
        np.sqrt((5 + 2*np.sqrt(10/7))/3)
    ])
    w = np.array([
        (322 - 13*np.sqrt(70))/900,
        (322 + 13*np.sqrt(70))/900,
        128/225,
        (322 + 13*np.sqrt(70))/900,
        (322 - 13*np.sqrt(70))/900
    ])
    x = (b - a)/2 * t + (a + b)/2
    return (b - a)/2 * np.sum(w * f(x))

# 示例：计算 ∫e^{-x^2} dx 在 [0, 1] 上的积分
f = lambda x: 1/1+x**4
a, b = 0, 1

I3 = gauss_legendre_3(f, a, b)
I5 = gauss_legendre_5(f, a, b)

print("三点高斯-勒让德近似值:", I3)
print("五点高斯-勒让德近似值:", I5)