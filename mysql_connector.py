import mysql.connector
from datetime import date  

# ข้อมูลการเชื่อมต่อฐานข้อมูล
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Mild',  
    'database': 'number one'
}

def add_new_user(name, email, phone):
    """ฟังก์ชันสำหรับเพิ่มข้อมูลผู้ใช้ใหม่ลงในตาราง 'users'."""
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        
        sql = "INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)"
        val = (name, email, phone)
        
        cursor.execute(sql, val)
        connection.commit()
        print(f"เพิ่มผู้ใช้ '{name}' สำเร็จแล้ว!")
        
    except mysql.connector.Error as error:
        print(f"เกิดข้อผิดพลาดในการเพิ่มข้อมูล: {error}")
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

def get_all_users():
    """ฟังก์ชันสำหรับดึงข้อมูลผู้ใช้ทั้งหมดจากตาราง 'users'."""
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        
        print("\n--- รายชื่อผู้ใช้ทั้งหมด ---")
        for user in users:
            # แก้ไขการแสดงผลเพื่อให้ตรงกับจำนวนและลำดับของคอลัมน์
            print(f"ID: {user[0]}, ชื่อ: {user[1]}, อีเมล: {user[2]}, เบอร์โทร: {user[3]}")
            
    except mysql.connector.Error as error:
        print(f"เกิดข้อผิดพลาดในการดึงข้อมูล: {error}")
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# --- การเรียกใช้ฟังก์ชัน ---
# ลองเพิ่มผู้ใช้ใหม่ด้วยข้อมูล name, email, และ phone
add_new_user("กัลยกร", "test@example.com", "099-123-4567")

# ลองแสดงข้อมูลผู้ใช้ทั้งหมด
get_all_users() 


import mysql.connector

# ข้อมูลการเชื่อมต่อฐานข้อมูล
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Mild',  # รหัสผ่านที่คุณใช้
    'database': 'number one'
}

def add_new_customer(name, email, phone, building):
    """
    ฟังก์ชันสำหรับเพิ่มข้อมูลลูกค้าใหม่ลงในตาราง 'customers'.
    """
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # แก้ไขคำสั่ง SQL ให้ตรงกับคอลัมน์ที่มีอยู่ (name, email, phone, building)
        sql = "INSERT INTO customers (name, email, phone, building) VALUES (%s, %s, %s, %s)" 
        val = (name, email, phone, building)
        
        cursor.execute(sql, val)
        connection.commit()
        print(f"เพิ่มข้อมูลลูกค้า {name} สำเร็จแล้ว!")
        
    except mysql.connector.Error as error:
        print(f"เกิดข้อผิดพลาดในการเพิ่มข้อมูล: {error}")
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# --- ตัวอย่างการใช้งาน ---
# เรียกใช้ฟังก์ชันเพื่อเพิ่มลูกค้าใหม่
add_new_customer("สมชาย", "somchai@example.com", "081-123-4567", "A")




def add_new_work_order(room_number, service_name, description, booking_date):
    """
    ฟังก์ชันสำหรับเพิ่มรายการแจ้งซ่อมใหม่
    booking_date ควรเป็น object date เช่น date.today()
    """
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # แก้ไขโค้ด SQL ให้ใช้คอลัมน์ที่ถูกต้องในตาราง work_orders
        sql = "INSERT INTO work_orders (room_number, service_name, description, booking_date) VALUES (%s, %s, %s, %s)"
        val = (room_number, service_name, description, booking_date)
        
        cursor.execute(sql, val)
        connection.commit()
        print(f"บันทึกรายการแจ้งซ่อมสำหรับห้อง {room_number} สำเร็จแล้ว!")
        
    except mysql.connector.Error as error:
        print(f"เกิดข้อผิดพลาดในการเพิ่มรายการแจ้งซ่อม: {error}")
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("ปิดการเชื่อมต่อแล้ว")

# --- ตัวอย่างการเรียกใช้ฟังก์ชัน ---

# ลองเพิ่มรายการแจ้งซ่อมใหม่
add_new_work_order(101, "ระบบไฟฟ้า", "หลอดไฟในห้องเสีย", date.today())



def add_cleaning_service(service_name, description):
    """ฟังก์ชันสำหรับบันทึกรายการทำความสะอาดใหม่"""
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # ตรวจสอบว่าการเชื่อมต่อสำเร็จ
        if connection.is_connected():
            print("เชื่อมต่อสำเร็จแล้ว! กำลังเพิ่มรายการทำความสะอาด...")
            
            # คำสั่ง SQL สำหรับเพิ่มข้อมูล
            sql = "INSERT INTO services (service_name, description, booking_date) VALUES (%s, %s, %s)"
            
            # ข้อมูลที่จะเพิ่ม
            # service_name: ชื่อบริการ (เช่น "ทำความสะอาดห้อง")
            # description: รายละเอียด (เช่น "ต้องการทำความสะอาดใหญ่")
            # booking_date: วันที่ปัจจุบัน
            val = (service_name, description, date.today())
            
            cursor.execute(sql, val)
            connection.commit()
            print(f"บันทึกบริการ '{service_name}' สำเร็จแล้ว!")

    except mysql.connector.Error as error:
        print(f"เกิดข้อผิดพลาดในการเพิ่มข้อมูล: {error}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("ปิดการเชื่อมต่อแล้ว")

# --- ตัวอย่างการเรียกใช้งาน ---
add_cleaning_service("ทำความสะอาดห้อง", "ต้องการทำความสะอาดใหญ่ทั้งห้อง")



def add_payment(room_number, status, details):
    """ฟังก์ชันสำหรับเพิ่มรายการชำระเงินใหม่ลงในตาราง 'payments'."""
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # คำสั่ง SQL สำหรับเพิ่มข้อมูล
        sql = "INSERT INTO payments (room_number, issue_date, status, details) VALUES (%s, %s, %s, %s)"
        
        # ข้อมูลที่จะเพิ่ม
        # issue_date จะถูกตั้งเป็นวันที่ปัจจุบันโดยอัตโนมัติ
        val = (room_number, date.today(), status, details)
        
        cursor.execute(sql, val)
        connection.commit()
        print(f"บันทึกการชำระเงินสำหรับห้อง {room_number} สำเร็จแล้ว!")

    except mysql.connector.Error as error:
        print(f"เกิดข้อผิดพลาดในการบันทึกข้อมูล: {error}")

    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("ปิดการเชื่อมต่อแล้ว")

# --- ตัวอย่างการเรียกใช้งาน ---
# เพิ่มรายการชำระเงินใหม่
add_payment("103", "จ่ายแล้ว", "ชำระค่าห้องและค่าน้ำ")


def main_menu():
    while True:
        print("\n--- ระบบจัดการหอพัก ---")
        print("1. เพิ่มผู้ใช้ใหม่")
        print("2. เพิ่มรายการแจ้งซ่อม")
        print("3. ดูรายการชำระเงินทั้งหมด")
        print("4. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกเมนู (1-4): ")

        if choice == '1':
            # เรียกใช้ฟังก์ชันสำหรับเพิ่มผู้ใช้
            # ตัวอย่าง: add_new_user("user_name", "user_email", "user_phone")
            pass
        elif choice == '2':
            # เรียกใช้ฟังก์ชันสำหรับเพิ่มรายการแจ้งซ่อม
            # ตัวอย่าง: add_work_order("room_number", "service_name", "description", "email")
            pass
        elif choice == '3':
            # เรียกใช้ฟังก์ชันสำหรับดูรายการชำระเงิน
            # ตัวอย่าง: get_all_payments()
            pass
        elif choice == '4':
            print("ออกจากโปรแกรม...")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง")

# เรียกใช้เมนูหลักเมื่อโปรแกรมเริ่มทำงาน
main_menu()