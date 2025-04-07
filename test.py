from main import EmployeeDAO, Employee 
from datetime import datetime

if __name__ == "__main__":
    
    dao = EmployeeDAO()
    new_employee = Employee(
        None, 
        name="Aidin",
        position="CEO",
        salary=200000,  
        hire_date=datetime.now().strftime("%Y-%m-%d")
    )
    dao.insert(new_employee)
    print("Employee inserted with id:", new_employee.id)

    employ = dao.get_by_id(1)
    print("\nRetrieved employee by ID 1:", employ if employ else "Not found", "\n")

    all_employees = dao.get_all()
    print("All employees:")

    for employee in all_employees:
        print(employee)
    updated_employee = Employee(
        id=11,
        name="Bekzat",
        position="Sales",
        salary=100,  
        hire_date=datetime.now().strftime("%Y-%m-%d")
    )
    dao.update(updated_employee)
    print("\nEmployee updated. New data for ID 1:", dao.get_by_id(1))
    dao.delete(1)
    print("\nEmployee with ID 1 deleted.")

    all_employees = dao.get_all()
    print("\nAll employees after deletion:")
    for employee in all_employees:
        print(employee)
    dao.close()
