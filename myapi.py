# import fastapi
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
#from typing import ClassVar

app = FastAPI()

employees = {
    1:{
        "name":"john",
        "age": 17,
        "class":"year 12"
    }
}

class Employee(BaseModel):
    name: str
    age: int
    year: str

class UpdateEmployee(BaseModel):
    name: Optional[str] = None
    age : Optional[int] = None
    year: Optional[str] = None


@app.get("/")
def index():
    return {"name":"First Data"}

@app.get("/get-employee/{employee_id}")
def get_employee(employee_id: int = Path(None, description="The ID you wan to review", gt=0, lt=3)):
    return employees[employee_id]

@app.get("/get-by-name/{employee_id}")
def get_employee(*, employee_id : int, name : Optional[str] = None, test:int):
    for employee_id in employees:
        if employees[employee_id]["name"] == name:
            return employees[employee_id]
    return {"Data": "Not found"}

@app.post("/create-employee/{empolyee_id}")
def create_employee(employee_id:int, employee : Employee):
    if employee_id in employees:
        return {"Error" : "Employee exists"}

    employees[employee_id] = employee
    return employees[employee_id]

@app.put("/update-employee/{employee_id}")
def update_employee(employee_id:int, employee : UpdateEmployee) :
    if employee_id not in employees:
        return {"Error" : "Student does not exists"}

    if employee.name != None:
        employees[employee.name] = employee.name

    if employee.age != None:
        employees[employee.age] = employee.age

    if employee.year != None:
        employee[employee.year] = employee.year

    employees[employee_id] = employee
    return employees[employee_id]

@app.delete("/delete-employee/{employee_id}")
def delete_employee(employee_id: int):
    if employee_id not in employees:
        return {"Error" : "Employee does not exist"}
    del employees[employee_id]
    return {"Message": "Employee deleted successfully"}


# google.com/resultsa?search=Python

#gt = greater than
#lt = less than


# GET    - GET AN INFORAMTION
# POST   - CREATE ST NEW
# PUT    - UPDATE ST
# DELETE - DELETE ST
