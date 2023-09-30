import sqlite3

conn = sqlite3.connect('user_data.db')

cursor = conn.cursor()


sql_select = """
    SELECT * FROM users
"""


cursor.execute(sql_select)
print(cursor.fetchall())

conn.close()