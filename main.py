import sqlite3
from datetime import datetime

class Employee:
    def __init__(self, id, name, position, salary, hire_date):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.hire_date = hire_date

    def __str__(self):
        return f'Employee(id={self.id}, name="{self.name}", position="{self.position}", salary={self.salary}, hire_date="{self.hire_date}")'

class EmployeeDAO:
    def __init__(self, db_name="person.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                position TEXT,
                salary INTEGER,
                hire_date TEXT
            )
        ''')
        self.conn.commit()

    def insert(self, employee):
        self.cursor.execute('''
            INSERT INTO employee (name, position, salary, hire_date)
            VALUES (?, ?, ?, ?)
        ''', (employee.name, employee.position, employee.salary, employee.hire_date))
        self.conn.commit()
        employee.id = self.cursor.lastrowid

    def get_by_id(self, id):
        self.cursor.execute('SELECT * FROM employee WHERE id = ?', (id,))  
        row = self.cursor.fetchone()
        if row:
            return Employee(*row)
        return None

    def get_all(self):
        self.cursor.execute('SELECT * FROM employee')
        rows = self.cursor.fetchall()
        return [Employee(*row) for row in rows]

    def update(self, employee):
        self.cursor.execute('''
            UPDATE employee
            SET name = ?, position = ?, salary = ?, hire_date = ?
            WHERE id = ?
        ''', (employee.name, employee.position, employee.salary, employee.hire_date, employee.id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute('DELETE FROM employee WHERE id = ?', (id,)) 
        self.conn.commit()

    def delete_all(self):
        self.cursor.execute("DELETE FROM employee")
        self.cursor.execute("DELETE FROM sqlite_sequence WHERE name='employee'")
        self.conn.commit()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    dao = EmployeeDAO()

    print("Current employees in database:")
    employees = dao.get_all()
    if employees:
        for emp in employees:
            print(emp)
    else:
        print("No employees in database yet.")

    while True:
        print("\nMENU OPTIONS")
        print("1. Insert employee")
        print("2. Get employee by id")
        print("3. Get all employees")
        print("4. Update employee")
        print("5. Delete employee")
        print("6. Delete all employees")
        print("7. Exit")

        choice = int(input("Enter your choice (1,2,3,4,5,6,7): "))

        if choice == 1:
            name = input("Enter name: ")
            position = input("Enter position: ")
            salary = int(input("Enter salary: "))
            hire_date = datetime.now().strftime("%Y-%m-%d")
            employee = Employee(None, name, position, salary, hire_date)
            dao.insert(employee)
            print(f"Employee inserted with id {employee.id}")

        elif choice == 2:
            id1 = int(input("Enter id: "))
            employee = dao.get_by_id(id1)
            if employee:
                print(employee)
            else:
                print(f"Employee with id {id1} not found")

        elif choice == 3:
            employees = dao.get_all()
            if employees:
                for employee in employees:
                    print(employee)
            else:
                print("No employees found")

        elif choice == 4:
            id = int(input("Enter updated id: "))
            name = input("Enter updated name: ")
            position = input("Enter updated position: ")
            salary = int(input("Enter updated salary: "))
            hire_date = datetime.now().strftime("%Y-%m-%d")
            employee = Employee(id, name, position, salary, hire_date)
            dao.update(employee)
            print("Employee updated successfully")

        elif choice == 5:
            id = int(input("Enter id to delete: "))
            dao.delete(id)
            print("Employee deleted successfully")

        elif choice == 6:
            dao.delete_all()
            print("All employees deleted successfully")

        elif choice == 7:
            print("Exiting...")
            dao.close()
            break

        else:
            print("Invalid choice. Please try again")