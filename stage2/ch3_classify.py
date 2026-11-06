import numpy as np

minutes = np.array([45, 30, 60, 25, 50, 40, 35, 55, 20, 70], dtype=float)
passed = np.array([1, 1, 1, 0, 1, 1, 0, 1, 0, 1], dtype=float)   # 正确率 >= 0.7 记 1

x_mean, x_std = minutes.mean(), minutes.std()
xs = (minutes - x_mean) / x_std


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def train(xs, ys, lr=0.5, steps=300):
    w, b = 0.0, 0.0
    for _ in range(steps):
        p = sigmoid(w * xs + b)
        dw = ((p - ys) * xs).mean()
        db = (p - ys).mean()
        w -= lr * dw
        b -= lr * db
    return w, b


def predict(w, b, values):
    p = sigmoid(w * values + b)
    return (p >= 0.5).astype(int), p


train_mask = np.array([True, True, True, True, True, True, True, False, False, False])
test_mask = ~train_mask

w, b = train(xs[train_mask], passed[train_mask])
pred_train, _ = predict(w, b, xs[train_mask])
pred_test, prob_test = predict(w, b, xs[test_mask])

acc_train = (pred_train == passed[train_mask]).mean()
acc_test = (pred_test == passed[test_mask]).mean()

print(f"训练集 {train_mask.sum()} 条，准确率 {acc_train:.0%}")
print(f"测试集 {test_mask.sum()} 条，准确率 {acc_test:.0%}")
for m, p, t in zip(minutes[test_mask], prob_test, passed[test_mask]):
    print(f"时长 {m:.0f} → 概率 {p:.2f}，预测 {int(p >= 0.5)}，真实 {int(t)}")
print(f"分界线约在 {x_mean + (-b / w) * x_std:.1f} 分钟")
