import sqlite3

class DBAccess:
    def __init__(self):
        self.conn = sqlite3.connect(r'objects.db')
        self.c = self.conn.cursor()
        self.create_characters_table()
        self.create_items_table()
        self.commit()


    def create_characters_table(self):
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS characters
                        (name TEXT PRIMARY KEY,
                        max_health INTEGER,
                        stat_attack INTEGER,
                        stat_defence INTEGER,
                        inventory TEXT,
                        gold INTEGER)''')


    def create_items_table(self):
        self.c.execute(f'''CREATE TABLE IF NOT EXISTS items
                        (name TEXT PRIMARY KEY,
                        value INTEGER,
                        max_health_up INTEGER,
                        health_up INTEGER,
                        stat_attack_up INTEGER,
                        stat_defence_up INTEGER)''')


    def commit(self):
        self.conn.commit()


    def close(self):
        self.conn.close()


    def fetch_single_stat(self, table, row_name, stat_name):
        return self.c.execute(f"SELECT {stat_name} FROM {table} WHERE name = '{row_name}'").fetchone()[0]


    def fetch_row(self, table, row_name):
        return self.c.execute(f"SELECT * FROM {table} WHERE name = '{row_name}'").fetchall()[0]


    def fetch_names(self, table):
        names = self.c.execute(f"SELECT name FROM {table}").fetchall()
        return [name[0] for name in names]


    def fetch_column_names(self, table):
        columns = self.c.execute(f'SELECT * FROM {table}')
        return [description[0] for description in columns.description]


    def insert_row(self, table, values):
        values = "','" .join(values)
        self.c.execute(f"INSERT OR IGNORE INTO {table} VALUES ('{values}')")
        self.commit()


    def update_value(self, table, row_name, stat_name, stat_value):
        self.c.execute(f"UPDATE {table} SET {stat_name} = '{stat_value}' WHERE name = '{row_name}'")
        self.commit()


    def delete_row(self, table, row_name):
        self.c.execute(f"DELETE FROM {table} WHERE name = '{row_name}'")
