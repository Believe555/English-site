import sqlite3
import datetime

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