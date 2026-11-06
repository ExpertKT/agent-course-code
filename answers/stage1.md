# 阶段一练习答案与边界用例

## 第 0 章 · most_common

```python
def most_common(text):
    counts = count_words(text)
    return min(counts, key=lambda w: (-counts[w], w))
```

边界：空文本返回 `None`；并列时取字典序靠前的词。

## 第 1 章 · two_sum([3, 3], 6)

应返回 `(0, 1)`。`seen` 先查后记，所以第二个 3 查到的是第一个 3 的下标，不会返回 `(0, 0)`。

边界：`[3]` 与目标 6 返回 `None`；空列表返回 `None`。

## 第 2 章 · 文件报告

`sample.txt` 是 12 字节、3 行、2 行非空。加一行“中文”后：18 或 19 字节取决于你保存时文件末尾有没有换行，所以不要背死数字，跑一次看结果。

边界：空文件返回 `lines=0, nonempty=0`，不是错误。

## 第 3 章 · report_all

```python
def report_all(directory):
    for path in sorted(Path(directory).glob("*.txt")):
        data = report(path)
        print(path.name, data["bytes"], data["lines"], data["nonempty"])
```

边界：目录不存在时抛 `FileNotFoundError` 或返回空列表，二选一，但要在 README 里写明。空目录打印 0 行。

## 第 4 章 · 线程竞态

删掉 `with lock` 后多跑几次，结果可能是 400，也可能偏小。这说明竞态不是每次都发生，不能靠“跑一次对了”当证据。

边界：线程数越多、每线程次数越多，越容易撞上。

## 第 5 章 · priority 列

```python
connection.execute("ALTER TABLE tasks ADD COLUMN priority INTEGER DEFAULT 0")
```

老数据库加列要用 `ALTER TABLE`；新库直接写进建表语句。边界：`ALTER TABLE` 在已有同名列时会报错，用 `IF NOT EXISTS` 不适用于加列，需要先查 `PRAGMA table_info(tasks)`。

## 第 6 章 · http_500 与陌生事件

```python
assert classify({"event": "http_500"})["retryable"] is True
assert classify({"event": "unknown_event"})["retryable"] is None
```

边界：`http_408` 属于可重试（超时类），`http_400` 属于不可重试。

## 第 7 章 · 评测扩到 20 条

边界：同一句话的多种正确说法会被关键词判错。先人工看失败清单，再决定是模型错还是标准错。
