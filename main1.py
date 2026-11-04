from fastapi import FastAPI

app = FastAPI()

employees = [
    {"id": 101, "name": "Rahul", "department": "Python", "salary": 30000},
    {"id": 102, "name": "Priya", "department": "SQL", "salary": 35000},
    {"id": 103, "name": "Kiran", "department": "Java", "salary": 40000}
]
@app.get("/")
def home():
    return {"message": "Welcome to Employee Management API"}

@app.get("/employees")
def get_employees():
    return employees