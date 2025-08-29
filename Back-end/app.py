from flask import Flask, jsonify, request
import mysql.connector
from datetime import date

# --- 1. Database Configuration ---
# Your database credentials from the previous code
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Mild', 
    'database': 'number one'
}

# --- 2. Flask App Initialization ---
app = Flask(__name__)

# Function to get a connection to the database
def get_db_connection():
    try:
        return mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# --- 3. API Endpoints ---
# Endpoints for 'users' table
@app.route('/api/users', methods=['GET', 'POST'])
def handle_users():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = conn.cursor(dictionary=True)
    try:
        if request.method == 'GET':
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            return jsonify(users), 200
        elif request.method == 'POST':
            new_user_data = request.json
            name = new_user_data.get('name')
            email = new_user_data.get('email')
            phone = new_user_data.get('phone')
            if not all([name, email, phone]):
                return jsonify({"error": "Missing required fields"}), 400
            
            sql = "INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)"
            val = (name, email, phone)
            cursor.execute(sql, val)
            conn.commit()
            return jsonify({"message": f"Successfully added user: {name}"}), 201
    except mysql.connector.Error as error:
        return jsonify({"error": f"Database error: {error}"}), 500
    finally:
        cursor.close()
        conn.close()

# Endpoints for 'customers' table
@app.route('/api/customers', methods=['GET', 'POST'])
def handle_customers():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    cursor = conn.cursor(dictionary=True)
    try:
        if request.method == 'GET':
            cursor.execute("SELECT * FROM customers")
            customers = cursor.fetchall()
            return jsonify(customers), 200
        elif request.method == 'POST':
            new_customer_data = request.json
            name = new_customer_data.get('name')
            email = new_customer_data.get('email')
            phone = new_customer_data.get('phone')
            building = new_customer_data.get('building')
            if not all([name, email, phone, building]):
                return jsonify({"error": "Missing required fields"}), 400
            sql = "INSERT INTO customers (name, email, phone, building) VALUES (%s, %s, %s, %s)"
            val = (name, email, phone, building)
            cursor.execute(sql, val)
            conn.commit()
            return jsonify({"message": f"Successfully added customer: {name}"}), 201
    except mysql.connector.Error as error:
        return jsonify({"error": f"Database error: {error}"}), 500
    finally:
        cursor.close()
        conn.close()

# Endpoints for 'work_orders' table
@app.route('/api/work_orders', methods=['GET', 'POST'])
def handle_work_orders():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    cursor = conn.cursor(dictionary=True)
    try:
        if request.method == 'GET':
            cursor.execute("SELECT * FROM work_orders")
            work_orders = cursor.fetchall()
            return jsonify(work_orders), 200
        elif request.method == 'POST':
            new_order_data = request.json
            room_number = new_order_data.get('room_number')
            service_name = new_order_data.get('service_name')
            description = new_order_data.get('description')
            booking_date = date.today()
            if not all([room_number, service_name, description]):
                return jsonify({"error": "Missing required fields"}), 400
            sql = "INSERT INTO work_orders (room_number, service_name, description, booking_date) VALUES (%s, %s, %s, %s)"
            val = (room_number, service_name, description, booking_date)
            cursor.execute(sql, val)
            conn.commit()
            return jsonify({"message": f"Successfully added work order for room: {room_number}"}), 201
    except mysql.connector.Error as error:
        return jsonify({"error": f"Database error: {error}"}), 500
    finally:
        cursor.close()
        conn.close()

# Endpoints for 'payments' table
@app.route('/api/payments', methods=['GET', 'POST'])
def handle_payments():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    cursor = conn.cursor(dictionary=True)
    try:
        if request.method == 'GET':
            cursor.execute("SELECT * FROM payments")
            payments = cursor.fetchall()
            return jsonify(payments), 200
        elif request.method == 'POST':
            new_payment_data = request.json
            room_number = new_payment_data.get('room_number')
            status = new_payment_data.get('status')
            details = new_payment_data.get('details')
            issue_date = date.today()
            if not all([room_number, status, details]):
                return jsonify({"error": "Missing required fields"}), 400
            sql = "INSERT INTO payments (room_number, issue_date, status, details) VALUES (%s, %s, %s, %s)"
            val = (room_number, issue_date, status, details)
            cursor.execute(sql, val)
            conn.commit()
            return jsonify({"message": f"Successfully added payment for room: {room_number}"}), 201
    except mysql.connector.Error as error:
        return jsonify({"error": f"Database error: {error}"}), 500
    finally:
        cursor.close()
        conn.close()

# Endpoints for 'services' table
@app.route('/api/services', methods=['GET', 'POST'])
def handle_services():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    cursor = conn.cursor(dictionary=True)
    try:
        if request.method == 'GET':
            cursor.execute("SELECT * FROM services")
            services = cursor.fetchall()
            return jsonify(services), 200
        elif request.method == 'POST':
            new_service_data = request.json
            service_name = new_service_data.get('service_name')
            description = new_service_data.get('description')
            booking_date = date.today()
            if not all([service_name, description]):
                return jsonify({"error": "Missing required fields"}), 400
            sql = "INSERT INTO services (service_name, description, booking_date) VALUES (%s, %s, %s, %s)"
            val = (service_name, description, booking_date)
            cursor.execute(sql, val)
            conn.commit()
            return jsonify({"message": f"Successfully added service: {service_name}"}), 201
    except mysql.connector.Error as error:
        return jsonify({"error": f"Database error: {error}"}), 500
    finally:
        cursor.close()
        conn.close()
        
# Endpoints for 'parcels' table
@app.route('/api/parcels', methods=['GET', 'POST'])
def handle_parcels():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Database connection failed"}), 500
    
    cursor = conn.cursor(dictionary=True)
    
    try:
        if request.method == 'GET':
            cursor.execute("SELECT * FROM parcels")
            parcels = cursor.fetchall()
            return jsonify(parcels), 200
        
        elif request.method == 'POST':
            new_parcel_data = request.json
            room_number = new_parcel_data.get('room_number')
            carrier = new_parcel_data.get('carrier')
            details = new_parcel_data.get('details')
            delivery_date = date.today()
            
            if not all([room_number, carrier, details]):
                return jsonify({"error": "Missing required fields"}), 400

            sql = "INSERT INTO parcels (room_number, delivery_date, carrier, details) VALUES (%s, %s, %s, %s)"
            val = (room_number, delivery_date, carrier, details)

            cursor.execute(sql, val)
            conn.commit()
            return jsonify({"message": f"Successfully added parcel for room: {room_number}"}), 201

    except mysql.connector.Error as error:
        print(f"Error handling parcels: {error}")
        return jsonify({"error": f"Database error: {error}"}), 500
    
    finally:
        if conn:
            cursor.close()
            conn.close()

# --- 4. Running the Flask App ---
if __name__ == '__main__':
    app.run(debug=True, port=5000)
