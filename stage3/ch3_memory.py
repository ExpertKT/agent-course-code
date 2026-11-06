import sqlite3
from pathlib import Path

db_path = Path("memory.db")
db_path.unlink(missing_ok=True)
db = sqlite3.connect(db_path)
db.execute("""CREATE TABLE messages (
    id INTEGER PRIMARY KEY,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
)""")

db.execute("INSERT INTO messages(role, content) VALUES (?, ?)", ("user", "我每天该学多久？"))
db.execute("INSERT INTO messages(role, content) VALUES (?, ?)", ("assistant", "建议每天 40 分钟。"))
db.execute("INSERT INTO messages(role, content) VALUES (?, ?)", ("user", "那算法练多久？"))
db.commit()

rows = db.execute("SELECT id, role, content FROM messages ORDER BY id").fetchall()
for row in rows:
    print(row)
print("条数：", len(rows))
