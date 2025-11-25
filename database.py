import sqlite3

def connect():
    return sqlite3.connect('warehouse.db')

def init_db():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS items (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            category TEXT NOT NULL,
                            quantity INTEGER NOT NULL,
                            code TEXT UNIQUE NOT NULL)''')
        conn.commit()

def add_item_db(item):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO items (name, category, quantity, code) VALUES (?, ?, ?, ?)',
                       (item.name, item.category, item.quantity, item.code))
        conn.commit()

def get_all_items():
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM items')
        return cursor.fetchall()

def search_items(query):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM items WHERE name LIKE ? OR category LIKE ? OR code LIKE ?',
                       (f'%{query}%', f'%{query}%', f'%{query}%'))
        return cursor.fetchall()

def delete_item(code):
    with connect() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM items WHERE code = ?', (code,))
        conn.commit()
