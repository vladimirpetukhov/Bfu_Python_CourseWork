import sqlite3


class DbContext:
    def __init__(self):
        self.conn = sqlite3.connect('./store.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)")
        self.conn.commit()


