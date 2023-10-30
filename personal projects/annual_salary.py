def annual_salary():
    total_hours = int(input("Please input your weekly hours: "))
    hourly = int(input("Please input your hourly wage: "))
    weekly = total_hours * hourly
    salary = weekly * 52
    return print("$" + str(salary))


annual_salary()
