import sqlite3

db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE messages (session_id TEXT, role TEXT, content TEXT)")

db.execute("INSERT INTO messages VALUES (?, ?, ?)", ("s1", "user", "我每天学多久？"))
db.execute("INSERT INTO messages VALUES (?, ?, ?)", ("s1", "assistant", "40 分钟。"))
db.execute("INSERT INTO messages VALUES (?, ?, ?)", ("s2", "user", "算法怎么练？"))

for session in ("s1", "s2"):
    rows = db.execute("SELECT role, content FROM messages WHERE session_id = ?", (session,)).fetchall()
    print(session, len(rows), rows[-1])
