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


# --- 1. ฟังก์ชันสำหรับเพิ่มข้อมูลพัสดุใหม่ ---
def add_new_parcel(room_number, delivery_date, carrier, details):
    """เพิ่มข้อมูลพัสดุใหม่ลงในตาราง 'parcels'"""
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        sql = "INSERT INTO parcels (room_number, delivery_date, carrier, details) VALUES (%s, %s, %s, %s)"
        val = (room_number, delivery_date, carrier, details)
        
        cursor.execute(sql, val)
        connection.commit()
        
        print(f"เพิ่มพัสดุสำหรับห้อง {room_number} สำเร็จ!")
        
    except mysql.connector.Error as err:
        print(f"เกิดข้อผิดพลาดในการเพิ่มข้อมูล: {err}")
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# --- 2. ฟังก์ชันสำหรับแสดงข้อมูลพัสดุทั้งหมด ---
def show_all_parcels():
    """แสดงข้อมูลพัสดุทั้งหมดจากตาราง 'parcels'"""
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM parcels")
        records = cursor.fetchall()
        
        if not records:
            print("ไม่พบข้อมูลพัสดุในระบบ")
            return
            
        print("\n--- รายการพัสดุทั้งหมด ---")
        for record in records:
            print(f"ID: {record[0]}, ห้อง: {record[1]}, วันที่: {record[2]}, บริษัท: {record[3]}, รายละเอียด: {record[4]}")
        print("----------------------------")
            
    except mysql.connector.Error as err:
        print(f"เกิดข้อผิดพลาดในการดึงข้อมูล: {err}")
    
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()

# --- ตัวอย่างการเรียกใช้งาน ---
if __name__ == "__main__":
    # เพิ่มข้อมูลพัสดุใหม่
    add_new_parcel("A-101", date(2025, 8, 29), "Kerry Express", "กล่องขนาดเล็ก, หนังสือ 1 เล่ม")
    add_new_parcel("B-205", date(2025, 8, 28), "Flash Express", "ซองเอกสารสำคัญ")
    add_new_parcel("C-302", date(2025, 8, 29), "Thai Post", "กล่องใหญ่, รองเท้า")
    
    # แสดงข้อมูลพัสดุทั้งหมดในตาราง
    show_all_parcels()    



def main_menu():
    while True:
        print("\n--- ระบบจัดการหอพัก ---")
        print("1. เพิ่มผู้ใช้ใหม่")
        print("2. เพิ่มรายการแจ้งซ่อม")
        print("3. ดูรายการชำระเงินทั้งหมด")
        print("4. ดูรายการพัสดุทั้งหมด")
        print("5. เพิ่มรายการพัสดุ")
        print("6. ออกจากโปรแกรม")
        
        choice = input("กรุณาเลือกเมนู (1-6): ")

        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            # Assuming you have a function to show all parcels
            pass
        elif choice == '5':
            # Collect data from user to add a new parcel
            room_number = input("ป้อนหมายเลขห้อง: ")
            carrier = input("ป้อนบริษัทขนส่ง: ")
            details = input("ป้อนรายละเอียด: ")
            
            # Automatically set the delivery date to today
            delivery_date = date.today()
            
            # Call the function to add the new parcel
            add_new_parcel(room_number, delivery_date, carrier, details)
        elif choice == '6':
            print("ออกจากโปรแกรม...")
            break
        else:
            print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง")

# Call the main menu when the program starts
if __name__ == "__main__":
    main_menu()




