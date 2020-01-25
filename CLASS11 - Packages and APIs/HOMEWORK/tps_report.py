# Your boss, Bill, asks you to come in on Saturday to finish your TPS report. You promise to finish the report, but as Bill walks away you
# smile knowing you have a trick up your sleeve: scripting! You plan on quickly mocking up a bit of code to finish the report and change
# your performance reviews in the system, all without spending a minute of your Saturday!
# You know of a Python module called csv that can be used to read and write csv files. CSV stands for "comma-separated values"
# and is a file type commonly associated with spreadsheets. You can check out the csv docs for examples of how this module
# works. We'll be using the DictWriter method, which maps a dictionary to output rows.

import csv
import os
os.system("clear")

employees = [{
    "first_name":"Bill",
    "last_name":"Lunmbergh",
    "job_title":"Vice President",
    "hire_date":'1985',
    "performance_review":"Excellent"
},{
    "first_name":"Michael",
    "last_name":"Bolton",
    "job_title":"Programmer",
    "hire_date":'1995',
    "performance_review":"Poor"
},{
    "first_name":"Peter",
    "last_name":"Gibbons",
    "job_title":"Programmer",
    "hire_date":'1989',
    "performance_review":"Poor"
},{
    "first_name":"Samir",
    "last_name":"Nagheenanajar",
    "job_title":"Programmer",
    "hire_date":'1974',
    "performance_review":"Fair"
},{
    "first_name":"Milton",
    "last_name":"Waddams",
    "job_title":"Collator",
    "hire_date":'1974',
    "performance_review":"Does he even work here?"
},{
    "first_name":"Bob",
    "last_name":"Porter",
    "job_title":"Consultant",
    "hire_date":'1999',
    "performance_review":"Excellent"
},{
    "first_name":"Bob",
    "last_name":"Slydell",
    "job_title":"Consultant",
    "hire_date":'1999',
    "performance_review":"Excellent"
}]

with open('tps_report.csv','w',newline='') as csvfile:

    # set names for the heater rows at the top
    header = ['first_name','last_name','job_title','hire_date','performance_review',"finished_review"]
    writer = csv.DictWriter(csvfile, fieldnames=header)
    
    writer.writeheader()
    for employee in employees:
        employee["finished_review"] = "yes"
        if employee["job_title"] == "Consultant" or employee["first_name"] == "Bill":
            employee["performance_review"] = "Poor"
        else: employee["performance_review"] = "Excellent"

        writer.writerow(employee)
    
