# Your boss tasks you with creating a company directory. Make a list called employees, which will
# contain one dictionary per person and include the keys name, age, department, phone, and salary.
# Once you have the list of dictionaries set up, loop through the list and print out the name,
# department, and phone number of each employee. Their age and salary should remain secret!
import os
import json
os.system("clear")

employees = [{
    "name" : "Ron Swanson",
    "age" : 55,
    "department" : "Managment",
    "phone" : "555-1234",
    "salary" : "$55,000"
},
{
    "name" : "Leslie Knope",
    "age" : 40,
    "department" : "Middle Managment",
    "phone" : "555-4321",
    "salary" : "$45,000"
},
{
    "name" : "Andy Dwyer",
    "age" : 22,
    "department" : "Shoe Shining",
    "phone" : "555-1122",
    "salary" : "$5,000"
},
{
    "name" : "April Ludgate",
    "age" : 19,
    "department" : "Administration",
    "phone" : "555-3345",
    "salary" : "$35,000"
}]

# print(json.dumps(employees,indent=1))

for employee in employees:
    print(employee["name"],"in",employee["department"],"can be reached at",employee["phone"]+".")