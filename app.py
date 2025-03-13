import sqlite3

# データベースに接続（存在しない場合は作成されます）
conn = sqlite3.connect('example.db')
c = conn.cursor()

# テーブルを作成
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# データの挿入
c.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
c.execute("INSERT INTO users (name, age) VALUES ('Bob', 25)")

# 変更を保存
conn.commit()

# データのクエリ
c.execute('SELECT * FROM users')
rows = c.fetchall()

# クエリ結果を表示
for row in rows:
    print(row)

# 接続を閉じる
conn.close()