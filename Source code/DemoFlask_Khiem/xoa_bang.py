import sqlite3

conn = sqlite3.connect('user_data.db')

cursor = conn.cursor()



#delete_table = """
#    DROP TABLE users;
#"""


#cursor.execute(delete_table)
conn.commit()

conn.close()