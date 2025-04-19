from flask import Flask, request, jsonify
import pymysql
import os

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST', 'mysql')
DB_USER = os.getenv('DB_USER', 'user')
DB_PASSWORD = os.getenv('DB_PASSWORD', '9118151707')
DB_NAME = os.getenv('DB_NAME', 'mysample')

def get_db_connection():
    return pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello, world!"})

@app.route('/write', methods=['POST'])
def write_data():
    data = request.json
    name = data.get('name')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Data inserted"}), 201

@app.route('/read', methods=['GET'])
def read_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT* from user")
    user = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify(user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)