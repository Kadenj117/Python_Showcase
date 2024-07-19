# import pandas python package to create data frames from csv file
import pandas as pd


# Employee class for each addition to the csv file
class Employee:
    def __init__(self, EmployeeID, Name, Department, Salary, Years):
        self.EmployeeID = EmployeeID
        self.Name = Name
        self.Department = Department
        self.Salary = Salary
        self.Years = Years

# Reads the csv file a creates a data frame with pandas
data_frame = pd.read_csv('employees.csv')

# list of all the employees in the csv file
employees = [
    Employee(
        row['EmployeeID'],
        row['Name'],
        row["Department"],
        row['Salary'],
        row['Years']
    ) for index, row in data_frame.iterrows()
]

# Generates and outputs Average salary, highest department average salary, and longest employee tenure
def Statistics(emp_list: list):
    print('__Statistics__')
    # calculates average salary of all the employees
    salary_avg = data_frame['Salary'].mean()

    print(f'Average Salary: {salary_avg}')

    # calculates average department salary and returns the highest average
    department_salary_avg = data_frame.groupby('Department')['Salary'].mean().reset_index()
    department_salary_avg.columns = ['Department', 'AverageSalary']
    highest_avg_salary = department_salary_avg.loc[department_salary_avg['AverageSalary'].idxmax()]

    print(f'Highest department average salary: {highest_avg_salary.Department}')
    print(department_salary_avg)

    # Finds the longest employee(s) tenure and returns the array
    longest_employees = []
    highest_years = 0
    for employ in emp_list:
        if employ.Years > highest_years:
            longest_employees = [employ.Name]
            highest_years = employ.Years
        elif employ.Years == highest_years:
            longest_employees.append(employ.Name)

    print(f'Longest employee(s) tenure: {longest_employees}')



Statistics(employees)
