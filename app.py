from flask import Flask, render_template, request
import psycopg2
import math

app = Flask(__name__)

# Database connection parameters
db_params = {
    'host': '192.168.56.20',
    'port': '5432',
    'dbname': 'csdashboard',
    'user': 'webuser1',
    'password': 'student',
}

def query_db(sql, params=None):
    """Query the database and return all records."""
    with psycopg2.connect(**db_params) as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params or ())
            return cur.fetchall()

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    search_query = request.args.get('search', '')
    sort_by = request.args.get('sort', 'Last')  # Sort by last name by default
    sort_order = request.args.get('order', 'asc')  # Default sort order
    per_page = 5
    offset = (page - 1) * per_page

    search_param = f'%{search_query}%'
    sql = f"""SELECT * FROM ecu_cs_dept_faculty 
              WHERE First ILIKE %s OR Last ILIKE %s 
              ORDER BY {sort_by} {sort_order} 
              LIMIT %s OFFSET %s;"""
    faculty_data = query_db(sql, (search_param, search_param, per_page, offset))

    total = query_db("SELECT COUNT(*) FROM ecu_cs_dept_faculty WHERE First ILIKE %s OR Last ILIKE %s;", (search_param, search_param))[0][0]
    pages = math.ceil(total / per_page)

    return render_template('index.html', faculty_data=faculty_data, page=page, pages=pages, total=total, search_query=search_query)

@app.route('/courses')
def courses():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    offset = (page - 1) * per_page

    courses_data = query_db("SELECT * FROM ecu_cs_dept_courses ORDER BY \"Prefix\", \"Number\" LIMIT %s OFFSET %s;", (per_page, offset))
    total = query_db("SELECT COUNT(*) FROM ecu_cs_dept_courses;")[0][0]

    pages = math.ceil(total / per_page)
    return render_template('courses.html', courses=courses_data, page=page, pages=pages)

@app.route('/fte')
def fte():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    offset = (page - 1) * per_page

    courses_data = query_db("SELECT * FROM ecu_cs_dept_courses ORDER BY \"Prefix\", \"Number\" LIMIT %s OFFSET %s;", (per_page, offset))
    total = query_db("SELECT COUNT(*) FROM ecu_cs_dept_courses;")[0][0]

    pages = math.ceil(total / per_page)
    return render_template('fte.html', courses=courses_data, page=page, pages=pages)

if __name__ == '__main__':
    app.run(debug=True)
