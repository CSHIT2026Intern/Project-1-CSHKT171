from flask import Flask, request, jsonify
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn_str = (
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=MSI;'                   # 對應截圖中的伺服器名稱
        'DATABASE=intern_project0701;'  # 你的資料庫名稱
        'UID=sa;'                       # 對應截圖中的登入帳號
        'PWD=Admin1234;'      # 請務必把這裡換成你登入 SSMS 用的那個密碼
        'TrustServerCertificate=yes;'   # 對應截圖中勾選的「信任伺服器憑證」
    )
    return pyodbc.connect(conn_str)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'success': False, 'message': '請輸入帳號與密碼'}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # pyodbc 使用 ? 作為參數化查詢的佔位符
        sql = "SELECT display_name, department, staff_id, email, system_role FROM users WHERE username = ? AND password = ?"
        cursor.execute(sql, (username, password))
        user = cursor.fetchone()

        if user:
            return jsonify({
                'success': True,
                'message': '登入成功',
                'data': {
                    'name': user.display_name,
                    'department': user.department,
                    'email': user.email,
                    'role': user.system_role
                }
            }), 200
        else:
            return jsonify({'success': False, 'message': '帳號或密碼錯誤，請重新輸入'}), 401

    except Exception as e:
        print(f"資料庫發生錯誤: {e}")
        return jsonify({'success': False, 'message': '伺服器發生異常'}), 500
        
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)