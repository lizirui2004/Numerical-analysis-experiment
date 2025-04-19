import torch

def newton_method(f, x0=3.14, tol=1e-4, max_iter=100):
    x = torch.tensor(float(x0), requires_grad=True)  # 确保转换为浮点数
    
    for i in range(max_iter):
        # 清零之前的梯度
        if x.grad is not None:
            x.grad.zero_()
        
        # 计算函数值
        fx = f(x)
        
        # 反向传播计算梯度
        fx.backward()
        
        # 获取梯度
        dfx = x.grad
        
        # 检查梯度
        if torch.abs(dfx) < 1e-8:  # 更安全的零值检查
            raise ValueError("导数为零，无法继续迭代")
        
        # 更新x值（需要脱离计算图）
        with torch.no_grad():
            x_new = x - fx / dfx
            delta = torch.abs(x_new - x)
            
            # 更新x值并保持requires_grad=True
            x.copy_(x_new)
        
        # 打印迭代信息
        print(f"Iter {i+1}: x = {x.item():.6f}, f(x) = {fx.item():.6f}, f'(x) = {dfx.item():.6f}")
        
        if delta < tol:
            print("\n达到精度要求，迭代终止")
            return x.item()  # 返回Python浮点数
    
    print("\n达到最大迭代次数，可能未收敛")
    return x.item()

# 定义函数
def f(x):
    return 12 - 3*x + 2*torch.cos(x)

if __name__ == "__main__":
    root = newton_method(f, 2.0)  # 使用更好的初始值2.0
    print(f"\n最终结果: {root:.8f}")