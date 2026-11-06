import math

KEYWORDS = ["算法", "结构", "线程", "文件", "数据库", "Agent", "模型", "日志", "上限", "重试"]

NOTES = [
    "二分查找每次砍掉一半，属于算法。",
    "哈希表用空间换时间，属于数据结构。",
    "线程共享数据要加锁，否则会丢更新。",
    "文件读写要指定编码，路径要用脚本位置。",
    "SQL 参数化能防注入，事务保证要么全成要么全回滚。",
    "Agent 要有步数上限和日志，模型调用要处理超时。",
    "循环没有上限会一直调用模型，必须设最大步数。",
    "工具失败就重试一次，两次都失败就记 error。",
]


def vector(text):
    return [text.count(word) for word in KEYWORDS]


def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return dot / (na * nb) if na and nb else 0.0


query = "Agent 为什么要设步数上限？"
qv = vector(query)
scores = [(cosine(qv, vector(note)), note) for note in NOTES]
scores.sort(reverse=True)

for score, note in scores[:3]:
    print(f"{score:.3f}  {note}")
