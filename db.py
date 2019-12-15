import sqlite3


class DbContext:
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




db = DbContext()
db.insert("4GB DDR4 Ram", "John Doe", "Microcenter", "160")
db.insert("Asus Mobo", "Mike Henry", "Microcenter", "360")
db.insert("500w PSU", "Karen Johnson", "Newegg", "80")
db.insert("2GB DDR4 Ram", "Karen Johnson", "Newegg", "70")
db.insert("24 inch Samsung Monitor", "Sam Smith", "Best Buy", "180")
db.insert("NVIDIA RTX 2080", "Albert Kingston", "Newegg", "679")
db.insert("600w Corsair PSU", "Karen Johnson", "Newegg", "130")


