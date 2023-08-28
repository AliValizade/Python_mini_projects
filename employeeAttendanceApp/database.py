import sqlite3

connection = sqlite3.connect('db/employee.db')
my_cursor = connection.cursor()

def create_table():
    my_cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            national_code TEXT,
            date_of_birth TEXT,
            face_image BLOB)
                        ''')
    connection.commit()

def save_employee(employee_data):
    my_cursor.execute('''
        INSERT INTO employees (first_name, last_name, national_code, date_of_birth, face_image)
        VALUES (?, ?, ?, ?, ?)
    ''', employee_data)
    connection.commit()

def getAll():
    employee_list = []
    my_cursor.execute('SELECT * FROM employees')
    results = my_cursor.fetchall()
    for employee in results:
        employee_list.append(employee)
    return employee_list

def page_rowsLimit(page_size, offset):
    my_cursor.execute("SELECT * FROM employees LIMIT ? OFFSET ?", (page_size, offset))
    results = my_cursor.fetchall()
    return results

def countEmployees():
    my_cursor.execute("SELECT COUNT(*) FROM employees")
    total_employees = my_cursor.fetchone()[0]
    return total_employees

def deleteEmployee(del_id):
    my_cursor.execute(f'DELETE FROM employees WHERE id={del_id}')
    connection.commit()
    
def editEmployee(employee, id):
    my_cursor.execute(f'UPDATE employees SET first_name={employee[1]}, last_name={employee[2]}, national_code={employee[3]} , date_of_birth={employee[4]} WHERE id={id}')
    connection.commit()