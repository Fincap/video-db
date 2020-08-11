import sqlite3

from db import DatabaseController

if __name__ == '__main__':
    conn = sqlite3.connect("data/tables.db")
    database_controller = DatabaseController(conn)
    print(database_controller.get_table_names())

    conn.close()
