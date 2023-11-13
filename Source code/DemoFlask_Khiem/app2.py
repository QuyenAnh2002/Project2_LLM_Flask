from re import template
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3






app = Flask(__name__)

app.static_folder = 'static' 
app.template_folder = 'templates'






# Hàm factory để tạo ứng dụng cho từng luồng
def create_app():

    # Kết nối đến cơ sở dữ liệu
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    return app, conn, cursor







@app.route('/register', methods=['GET', 'POST'])
def register():
    app, conn, cursor = create_app()  # Tạo ứng dụng và đối tượng kết nối
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']  # Thêm trường xác nhận mật khẩu

        cursor.execute('SELECT * FROM users WHERE username = ? ', (username, ))
        user = cursor.fetchone()  # Lấy dòng đầu tiên trùng khớp
        if user:
            return "Tài khoản đã tồn tại"
        else:
            if password == confirm_password:  # Kiểm tra mật khẩu và xác nhận mật khẩu trùng khớp
                cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
                conn.commit()
                conn.close()
                return redirect(url_for('login'))  # Chuyển hướng đến trang đăng nhập
            else:
                conn.close()
                return "Mật khẩu không trùng khớp. Vui lòng nhập lại."

    conn.close()
    return render_template('register.html')
    





@app.route('/login', methods=['GET', 'POST'])
def login():
    app, conn, cursor = create_app()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Kiểm tra xem thông tin đăng nhập có hợp lệ không
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()  # Lấy dòng đầu tiên trùng khớp
        
        if user:
            return redirect(url_for('home')) 
        else:
            return "Sai tên tài khoản hoặc mật khẩu!"

    conn.close()
    return render_template('login.html')





@app.route('/trangchu', methods=['GET', 'POST'])
def trangchu():
    app, conn, cursor = create_app()
    cursor.execute('SELECT id, name, path FROM img_data')
    images = cursor.fetchall()
    conn.close()
    return render_template('trangchu.html', images=images)



    
@app.route('/home', methods=['GET', 'POST'])
def home():
    app, conn, cursor = create_app()
    cursor.execute('SELECT id, name, path FROM img_data')
    images = cursor.fetchall()
    conn.close()
    return render_template('home.html', images=images)  
    


@app.route('/thanhtoan', methods=['GET', 'POST'])
def banggia():
    app, conn, cursor = create_app()
    cursor.execute('SELECT id, name, path FROM img_data')
    images = cursor.fetchall()
    conn.close()
    return render_template('banggia.html', images=images)  




@app.route('/001')
def t001():
    
    app, conn, cursor = create_app()

    
    cursor.execute('SELECT id, name, path FROM img_data')
    images = cursor.fetchall()

    conn.close()

    return render_template('001.html', images=images)





if __name__ == '__main__':
    #app, conn, cursor = create_app()  # Tạo ứng dụng và đối tượng kết nối
    
    app.run(debug=True)
