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
    per_page = 5
    offset = (page - 1) * per_page
    search_query = request.args.get('search', '')
    sort_by = request.args.get('sort', 'Last')
    sort_order = request.args.get('order', 'asc')

    search_param = f'%{search_query}%'
    sql = f"""SELECT * FROM ecu_cs_dept_faculty WHERE First ILIKE %s OR Last ILIKE %s ORDER BY {sort_by} {sort_order} LIMIT %s OFFSET %s;"""
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
    search_name = request.args.get('search_name', '')  # This will take either first or last name
    year = request.args.get('year')
    semester = request.args.get('semester')
    sort_by = request.args.get('sort', 'faculty')
    sort_order = request.args.get('order', 'asc')

    params = []
    where_clauses = []

    if search_name:
        where_clauses.append('(df.first ILIKE %s OR df.last ILIKE %s)')
        params.extend([f'%{search_name}%', f'%{search_name}%'])
    if year:
        where_clauses.append('csh.year = %s')
        params.append(year)
    if semester:
        where_clauses.append('csh.semester = %s')
        params.append(semester)

    where_clause = ' AND '.join(where_clauses) if where_clauses else '1=1'

    sql = f"""
    SELECT
        df."id",
        df."honorific" || ' ' || df."first" || ' ' || df."last" AS "faculty",
        csh."semester",
        csh."year",
        ROUND(SUM(
            CASE
                WHEN dc."Prefix" = 'CSCI' AND dc."GU" = 'G' THEN (dc."CH" * csh."enrollment")/186.23
                WHEN dc."Prefix" = 'CSCI' AND dc."GU" = 'U' THEN (dc."CH" * csh."enrollment")/406.24
                WHEN dc."Prefix" = 'SENG' AND dc."GU" = 'G' THEN (dc."CH" * csh."enrollment")/90.17
                WHEN dc."Prefix" = 'SENG' AND dc."GU" = 'U' THEN (dc."CH" * csh."enrollment")/232.25
                WHEN dc."Prefix" = 'DASC' THEN (dc."CH" * csh."enrollment")/186.23
                ELSE 0
            END), 2) AS "FTE"
    FROM
        "ecu_cs_dept_course_schedule_history" csh
    JOIN
        "ecu_cs_dept_faculty" df ON csh."instructor" = df."id"
    JOIN
        "ecu_cs_dept_courses" dc ON csh."prefix" = dc."Prefix" AND csh."number" = dc."Number"
    WHERE
        {where_clause}
    GROUP BY
        df."id", df."honorific", df."first", df."last", csh."semester", csh."year"
    ORDER BY
        {sort_by} {sort_order}
    LIMIT %s OFFSET %s;
    """

    params.extend([per_page, offset])

    fte_data = query_db(sql, params)

    # Count total records
    total_query = f"""
    SELECT COUNT(*) FROM "ecu_cs_dept_course_schedule_history" csh
    JOIN "ecu_cs_dept_faculty" df ON csh."instructor" = df."id"
    JOIN "ecu_cs_dept_courses" dc ON csh."prefix" = dc."Prefix" AND csh."number" = dc."Number"
    WHERE {where_clause};
    """
    total = query_db(total_query, params[:-2])[0][0]  # params[:-2] to exclude limit and offset
    pages = total // per_page
    if total % per_page > 0:
        pages += 1

    return render_template('fte.html', fte=fte_data, page=page, pages=pages, search_name=search_name, year=year, semester=semester)



if __name__ == '__main__':
    app.run(debug=True)