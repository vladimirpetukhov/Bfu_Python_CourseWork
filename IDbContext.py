import sqlite3


class IDbContext:
    def __init__(self):
        self.conn = sqlite3.connect('./store.db')
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS parts (id INTEGER PRIMARY KEY, [name] text, customer text, retailer text, price text)")
        self.conn.commit()

    
    def insert(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?, ?, ?, ?)",
                         (part, customer, retailer, price))
        self.conn.commit()


    def fetch(self):
        self.cur.execute("SELECT * FROM parts")
        rows = self.cur.fetchall()
        return rows


    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()

    
    def get_part(self,id):
        self.cur.execute("SELECT * FROM parts WHERE id=?", (id,))
        
        part=self.cur.fetchone()
        return part