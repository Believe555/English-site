import sqlite3
import datetime
import json

def init_db():
    conn = sqlite3.connect('english.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT NOT NULL,
            meaning TEXT NOT NULL
        )
    ''')
    cursor.execute("SELECT COUNT(*) FROM words")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO words (word, meaning) VALUES ('abandon', 'v. 放弃，抛弃')")
        cursor.execute("INSERT INTO words (word, meaning) VALUES ('benefit', 'n. 益处 v. 有益于')")
        cursor.execute("INSERT INTO words (word, meaning) VALUES ('crucial', 'adj. 至关重要的')")
    conn.commit()
    conn.close()

def get_random_word():
    conn = sqlite3.connect('english.db')
    cursor = conn.cursor()
    cursor.execute("SELECT word, meaning FROM words ORDER BY RANDOM() LIMIT 1")
    result = cursor.fetchone()
    conn.close()
    if result:
        return {"word": result[0], "meaning": result[1]}
    return {"word": "空", "meaning": "空"}

def init_checkin_db():
    conn = sqlite3.connect('english.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS checkins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_checkin():
    today = datetime.date.today().strftime("%Y-%m-%d")
    conn = sqlite3.connect('english.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO checkins (date) VALUES (?)", (today,))
    conn.commit()
    conn.close()




def import_words_from_json():
    try:
        with open('words.json', 'r', encoding='utf-8') as file:
            words_data = json.load(file)
    except Exception as e:
        print("读取 words.json 失败:", e)
        return

    conn = sqlite3.connect('english.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM words")  # 清空旧词

    for item in words_data:
        cursor.execute(
            "INSERT INTO words (word, meaning) VALUES (?, ?)",
            (item['word'], item['meaning'])
        )
    conn.commit()
    conn.close()
    print(f"🎉 成功从 words.json 导入了 {len(words_data)} 个单词！")