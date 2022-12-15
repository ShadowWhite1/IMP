from application import salary 
from application.db import people
import datetime
import time

DateCreation = datetime.datetime.today().strftime("%d.%m.%Y")
TimeCreation = time.strftime("%H:%M:%S")

print("Время: ", TimeCreation)
print("Дата: ", DateCreation, '\n')

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
