from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_mysqldb import MySQL
from datetime import datetime

# สร้าง Flask App
app = Flask(__name__)
# เปิดใช้งาน CORS เพื่อให้ Frontend เรียกใช้งานได้
CORS(app) 

# ตั้งค่า MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mild' # กรุณาตรวจสอบให้แน่ใจว่ารหัสผ่านนี้ถูกต้อง
app.config['MYSQL_DB'] = 'number one'

mysql = MySQL(app)

# ฟังก์ชันช่วยเหลือสำหรับตรวจสอบการเชื่อมต่อฐานข้อมูล
def check_db_connection():
    try:
        # ตรวจสอบว่าสามารถเชื่อมต่อฐานข้อมูลได้หรือไม่
        print("กำลังตรวจสอบการเชื่อมต่อฐานข้อมูล...")
        mysql.connection.ping(reconnect=True)
        print("เชื่อมต่อฐานข้อมูลสำเร็จ!")
        return True
    except Exception as e:
        # พิมพ์ข้อผิดพลาดที่เกิดขึ้นลงใน console เพื่อการแก้ไขปัญหา
        print(f"การเชื่อมต่อฐานข้อมูลล้มเหลว: {e}")
        return False

# --- API Endpoints ---
@app.route('/api/customers', methods=['GET', 'POST'])
def handle_customers():
    if not check_db_connection():
        return jsonify({"error": "การเชื่อมต่อฐานข้อมูลล้มเหลว: โปรดตรวจสอบสถานะ MySQL และข้อมูลการเข้าสู่ระบบ"}), 503
    try:
        cursor = mysql.connection.cursor()
        if request.method == 'GET':
            cursor.execute("SELECT * FROM customers")
            data = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            customers = [dict(zip(column_names, row)) for row in data]
            return jsonify(customers)
        
        elif request.method == 'POST':
            new_customer = request.json
            name = new_customer.get('name')
            email = new_customer.get('email')
            phone = new_customer.get('phone')
            
            cursor.execute("INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)", (name, email, phone))
            mysql.connection.commit()
            return jsonify({"message": "เพิ่มลูกค้าสำเร็จ!"}), 201
            
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการจัดการลูกค้า: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/api/payments', methods=['GET'])
def get_payments():
    if not check_db_connection():
        return jsonify({"error": "การเชื่อมต่อฐานข้อมูลล้มเหลว: โปรดตรวจสอบสถานะ MySQL และข้อมูลการเข้าสู่ระบบ"}), 503
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM payments")
        data = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        payments = [dict(zip(column_names, row)) for row in data]
        return jsonify(payments)
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการดึงข้อมูลการชำระเงิน: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/api/parcels', methods=['GET', 'POST'])
def handle_parcels():
    if not check_db_connection():
        return jsonify({"error": "การเชื่อมต่อฐานข้อมูลล้มเหลว: โปรดตรวจสอบสถานะ MySQL และข้อมูลการเข้าสู่ระบบ"}), 503
    try:
        cursor = mysql.connection.cursor()
        if request.method == 'GET':
            cursor.execute("SELECT * FROM parcels")
            data = cursor.fetchall()
            column_names = [i[0] for i in cursor.description]
            parcels = [dict(zip(column_names, row)) for row in data]
            return jsonify(parcels)
        
        elif request.method == 'POST':
            new_parcel = request.json
            room_number = new_parcel.get('room_number')
            carrier = new_parcel.get('carrier')
            details = new_parcel.get('details')
            
            cursor.execute("INSERT INTO parcels (room_number, carrier, details) VALUES (%s, %s, %s)", (room_number, carrier, details))
            mysql.connection.commit()
            return jsonify({"message": "เพิ่มพัสดุสำเร็จ!"}), 201
            
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการจัดการพัสดุ: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
