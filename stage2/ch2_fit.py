import numpy as np

x = np.array([45, 30, 60, 25, 50, 40, 35, 55, 20, 70], dtype=float)
y = np.array([0.80, 0.70, 0.90, 0.60, 0.85, 0.75, 0.65, 0.95, 0.55, 0.88], dtype=float)

x_mean, x_std = x.mean(), x.std()
y_mean, y_std = y.mean(), y.std()
xs = (x - x_mean) / x_std
ys = (y - y_mean) / y_std

w, b = 0.0, 0.0
lr = 0.1
for step in range(200):
    pred = w * xs + b
    loss = ((pred - ys) ** 2).mean()
    dw = 2 * ((pred - ys) * xs).mean()
    db = 2 * (pred - ys).mean()
    w -= lr * dw
    b -= lr * db
    if step % 50 == 0:
        print(f"step {step:3d} loss {loss:.4f}")

slope = w * y_std / x_std
intercept = y_mean + y_std * b - slope * x_mean
print(f"final w={w:.3f} b={b:.3f} loss={loss:.4f}")
print(f"换算成原始单位：正确率 ≈ {slope:.4f} * 时长 + {intercept:.3f}")
print(f"学 40 分钟，预测正确率 {slope * 40 + intercept:.2f}")
print(f"学 70 分钟，预测正确率 {slope * 70 + intercept:.2f}")
