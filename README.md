# Employee Management System 
## How to Run the Project

### 1. Clone the repository:  
    git clone https://github.com/your-username/your-repo-name.git  

### 2. Navigate to the project directory:  
    cd your-repo-name  

### 3. Make sure Python 3 is installed:  
    python --version  

### 4. Run the project: 
    
    python employee.py  

After running the program, you will see a menu:  

    MENU OPTIONS  
    1. Insert employee  
    2. Get employee by id  
    3. Get all employees  
    4. Update employee  
    5. Delete employee  
    6. Delete all employees  
    7. Exit
## Features
- Add new employees with name, position, salary, and hire date.
- Find employees by ID or list all employees.
- Update existing employee records.
- Delete individual employees or all records.
- Store data in a SQLite database (`people.db`).
- 
# Classes and Methods
### Below is an overview of the main classes and their methods in main.py:
# Employee Class
 Represents an employee with their details.
 __init__(self, id, name, position, salary, hire_date)
 Creates an employee object.

## Parameters:
 id: Integer (can be None for new employees, auto-assigned by database).

 name: String, employee's name.

 position: String, employee's job title.

 salary: Integer, employee's salary.

 hire_date: String, date of hiring in "YYYY-MM-DD" format.

## __str__(self)
 Returns a string representation of the employee, e.g., Employee(id=1, name="Argen", position="Programmer", salary=60000,  hire_date="2025-04-07").

# EmployeeDAO Class
 ### Handles database operations for employees using SQLite.
 ### __init__(self, db_name="employees2.db")
 ### Initializes a connection to the SQLite database and creates the employee table if it doesn’t exist.

## Parameter:
 ### db_name: String, name of the database file (default: "employees2.db").

 ### create_table(self)
 Creates the employee table with columns: id (auto-incremented), name, position, salary, and hire_date.

### insert(self, employee)
 Adds a new employee to the database.

## Parameter:
employee: An Employee object.

Updates the employee.id with the auto-generated ID.

get_by_id(self, id)
Retrieves an employee by their ID.

Parameter:
id: Integer, the employee’s ID.

Returns: Employee object or None if not found.

get_all(self)
Retrieves all employees from the database.

Returns: List of Employee objects.

update(self, employee)
Updates an existing employee’s details in the database.

Parameter:
employee: An Employee object with updated data.

delete(self, id)
Deletes an employee by their ID.

Parameter:
id: Integer, the employee’s ID.

delete_all(self)
Deletes all employees from the database and resets the ID counter.

close(self)
Closes the connection to the database.



## Requirements
- Python 3.x

## sample input and output
1. insert employee
   ```bash
   MENU OPTIONS
   MENU OPTIONS
   1. Insert employee
   2. Get employee by id
   3. Get all employees
   4. Update employee
   5. Delete employee
   6. Delete all employees
   7. Exit
   Enter your choice (1,2,3,4,5,6,7): 1
   Enter name: Kiril
   Enter position: wORKER
   Enter salary: 20000
   Employee inserted with id 1
2. Get employee bi id
   ```bash
   MENU OPTIONS
   1. Insert employee
   2. Get employee by id
   3. Get all employees
   4. Update employee
   5. Delete employee
   6. Delete all employees
   7. Exit
   Enter your choice (1,2,3,4,5,6,7): 2
   Enter id: 1
   Employee(id=1, name="Kiril", position="wORKER", salary=20000, hire_date="2025-04-07")
3. Get all employees
   ```bash
   MENU OPTIONS
   1. Insert employee
   2. Get employee by id
   3. Get all employees
   4. Update employee
   5. Delete employee
   6. Delete all employees
   7. Exit
   Enter your choice (1,2,3,4,5,6,7): 3
   Employee(id=1, name="Kiril", position="wORKER", salary=20000, hire_date="2025-04-07")
   Employee(id=2, name="Argen", position="Ceo", salary=30000, hire_date="2025-04-07")
   Employee(id=3, name="Magomed", position="Programer", salary=100000, hire_date="2025-04-07")
   Employee(id=4, name="Argen", position="Worker", salary=10000, hire_date="2025-04-07")
   Employee(id=5, name="Nuraali", position="Founder", salary=1000000, hire_date="2025-04-07")
   Employee(id=6, name="Meerim", position="HR", salary=70000, hire_date="2025-04-07")
   Employee(id=7, name="Aidin", position="President", salary=1000000, hire_date="2025-04-07")
4. Update employee
   ```bash
   MENU OPTIONS
   1. Insert employee
   2. Get employee by id
   3. Get all employees
   4. Update employee
   5. Delete employee
   6. Delete all employees
   7. Exit
   Enter your choice (1,2,3,4,5,6,7): 4
   Enter updated id: 5
   Enter updated name: Mirbek
   Enter updated position: Fufler
   Enter updated salary: 20000
   Employee updated successfully
5. Delate employee
   ```bash
   MENU OPTIONS
   1. Insert employee
   2. Get employee by id
   3. Get all employees
   4. Update employee
   5. Delete employee
   6. Delete all employees
   7. Exit
   Enter your choice (1,2,3,4,5,6,7): 5
   Enter id to delete: 2
   Employee deleted successfully
6. Table
   
<img width="939" alt="Screenshot 2025-04-07 at 10 54 38 PM" src="https://github.com/user-attachments/assets/0ed42277-b844-4c27-a43b-e129c6fce26f" />


 
    

   c

  
