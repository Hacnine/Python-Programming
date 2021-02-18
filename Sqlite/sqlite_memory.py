import sqlite3
from employee import Employee

# To enable: Shift+Ctrl+Alt+J
# To disable: SHIFT+ALT+INSERT
connection = sqlite3.connect(':memory:')
carsor = connection.cursor()

carsor.execute("""  CREATE TABLE employee (
                        first text,
                        last text,
                        pay integer

                        )""")


def insert_emp(emp):
    with connection:
        carsor.execute("INSERT INTO employee VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    carsor.execute("SELECT * FROM employee WHERE last=:last", {'last': lastname})
    return carsor.fetchall()


def update_pay(emp, pay):
    with connection:
        carsor.execute("""UPDATE employee SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with connection:
        carsor.execute("DELETE from employee WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 95000)
remove_emp(emp_1)

emps = get_emps_by_name()
print(emps)

connection.close()
