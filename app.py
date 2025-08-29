from flask import Flask, jsonify, request
import mysql.connector
from datetime import date

# Create the Flask application
app = Flask(__name__)

# Database connection configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Mild',
    'database': 'number one'  # Use a database name without spaces
}

def get_db_connection():
    """
    Establishes and returns a database connection.
    Returns None if a connection error occurs.
    """
    try:
        return mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None

# --- API Endpoint for Users (GET and POST) ---
@app.route('/api/users', methods=['GET', 'POST'])
def handle_users():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Cannot connect to the database"}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)

        if request.method == 'POST':
            # Add a new user
            new_user = request.json
            name = new_user.get('name')
            email = new_user.get('email')
            phone = new_user.get('phone')

            if not all([name, email, phone]):
                return jsonify({"error": "Incomplete data"}), 400

            sql = "INSERT INTO users (name, email, phone) VALUES (%s, %s, %s)"
            val = (name, email, phone)
            cursor.execute(sql, val)
            connection.commit()
            return jsonify({"message": f"Successfully added user: {name}!"}), 201

        elif request.method == 'GET':
            # Get all users
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            return jsonify(users)

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        connection.close()

# --- API Endpoint for Customers (GET and POST) ---
@app.route('/api/customers', methods=['GET', 'POST'])
def handle_customers():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Cannot connect to the database"}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)

        if request.method == 'POST':
            # Add a new customer
            new_customer = request.json
            name = new_customer.get('name')
            email = new_customer.get('email')
            phone = new_customer.get('phone')
            building = new_customer.get('building')

            if not all([name, email, phone, building]):
                return jsonify({"error": "Incomplete data"}), 400

            sql = "INSERT INTO customers (name, email, phone, building) VALUES (%s, %s, %s, %s)"
            val = (name, email, phone, building)
            cursor.execute(sql, val)
            connection.commit()
            return jsonify({"message": f"Successfully added customer: {name}!"}), 201

        elif request.method == 'GET':
            # Get all customers
            cursor.execute("SELECT * FROM customers")
            customers = cursor.fetchall()
            return jsonify(customers)

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        connection.close()

# --- API Endpoint for Work Orders (GET and POST) ---
@app.route('/api/work-orders', methods=['GET', 'POST'])
def handle_work_orders():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Cannot connect to the database"}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)

        if request.method == 'POST':
            # Add a new work order
            new_order = request.json
            room_number = new_order.get('room_number')
            service_name = new_order.get('service_name')
            description = new_order.get('description')
            email = new_order.get('email')

            if not all([room_number, service_name, description, email]):
                return jsonify({"error": "Incomplete data"}), 400

            sql = "INSERT INTO work_orders (room_number, service_name, description, email, booking_date) VALUES (%s, %s, %s, %s, %s)"
            val = (room_number, service_name, description, email, date.today())
            cursor.execute(sql, val)
            connection.commit()
            return jsonify({"message": f"Successfully added work order for room {room_number}!"}), 201

        elif request.method == 'GET':
            # Get all work orders
            cursor.execute("SELECT * FROM work_orders")
            work_orders = cursor.fetchall()
            return jsonify(work_orders)

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        connection.close()

# --- API Endpoint for Payments (GET and POST) ---
@app.route('/api/payments', methods=['GET', 'POST'])
def handle_payments():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Cannot connect to the database"}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)

        if request.method == 'POST':
            # Add a new payment record
            new_payment = request.json
            room_number = new_payment.get('room_number')
            status = new_payment.get('status')
            details = new_payment.get('details')

            if not all([room_number, status, details]):
                return jsonify({"error": "Incomplete data"}), 400

            sql = "INSERT INTO payments (room_number, issue_date, status, details) VALUES (%s, %s, %s, %s)"
            val = (room_number, date.today(), status, details)
            cursor.execute(sql, val)
            connection.commit()
            return jsonify({"message": f"Successfully added payment for room {room_number}!"}), 201

        elif request.method == 'GET':
            # Get all payment records
            cursor.execute("SELECT * FROM payments")
            payments = cursor.fetchall()
            return jsonify(payments)

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        connection.close()

# --- API Endpoint for Services (GET and POST) ---
@app.route('/api/services', methods=['GET', 'POST'])
def handle_services():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Cannot connect to the database"}), 500
    
    try:
        cursor = connection.cursor(dictionary=True)

        if request.method == 'POST':
            # Add a new service record
            new_service = request.json
            service_name = new_service.get('service_name')
            description = new_service.get('description')

            if not all([service_name, description]):
                return jsonify({"error": "Incomplete data"}), 400

            sql = "INSERT INTO services (service_name, description, booking_date) VALUES (%s, %s, %s)"
            val = (service_name, description, date.today())
            cursor.execute(sql, val)
            connection.commit()
            return jsonify({"message": f"Successfully added service: {service_name}!"}), 201

        elif request.method == 'GET':
            # Get all service records
            cursor.execute("SELECT * FROM services")
            services = cursor.fetchall()
            return jsonify(services)

    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True)
