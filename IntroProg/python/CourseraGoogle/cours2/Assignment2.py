#!/usr/bin/env python3
import csv

def read_employees(file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data["Department"])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data
def write_report(dictionary, report_file):
    with open(report_file, "w+") as file:
        for k in sorted(dictionary):
            file.write(str(k) + ":" + str(dictionary[k]+'\n'))


employee_list = read_employees("/home/student-01-56aa814187fd/data/employees.csv")
dictionary = process_data(employee_list)
print(dictionary)
write_report(dictionary, "/home/student-01-56aa814187fd/data/report.txt")
