from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# Database connection parameters
db_params = {
    'host': '192.168.56.20',
    'port': '5432',
    'dbname': 'csdashboard',
    'user': 'webuser1',
    'password': 'student',
}

def fetch_faculty_data(offset=0, limit=5):
    connection = None
    cursor = None
    faculty_data = []

    try:
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        query = f"SELECT * FROM ecu_cs_dept_faculty LIMIT {limit} OFFSET {offset};"
        cursor.execute(query)

        faculty_data = cursor.fetchall()

    except psycopg2.Error as e:
        print(f"Error: Unable to connect to the database. {e}")

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    return faculty_data

@app.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    limit = 5
    offset = (page - 1) * limit

    faculty_data = fetch_faculty_data(offset, limit)
    return render_template('index.html', faculty_data=faculty_data, page=page)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
