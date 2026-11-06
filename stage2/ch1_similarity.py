import math

def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb)

vectors = {
    "算法练习": [3, 1, 0],
    "刷算法题": [2, 2, 0],
    "背单词": [0, 1, 3],
}

base = vectors["算法练习"]
for name, vec in vectors.items():
    print(name, round(cosine(base, vec), 3))
