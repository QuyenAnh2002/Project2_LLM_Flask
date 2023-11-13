import sqlite3
conn = sqlite3.connect('user_data.db')

cursor = conn.cursor()


sql_insert = """
    INSERT INTO users (username, password)
    VALUES ('phi', 'phi1234')
"""


def add_image(name,path):
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    # Thêm thông tin về bức ảnh vào bảng images
    cursor.execute("INSERT INTO img_data (name, path) VALUES (?, ?)", (name, path))

    conn.commit()
    conn.close()

# Sử dụng hàm add_image để thêm một bức ảnh mới
add_image("001","static/images/001.jpg")

#cursor.execute(sql_insert)
#conn.commit()

#try:
#    cursor.execute(add_image)
#    conn.commit()
#except:
#   print("lỗi")

conn.close()