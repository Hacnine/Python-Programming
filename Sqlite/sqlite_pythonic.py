import sqlite3
from employee import Employee
connection = sqlite3.connect('employee.db')

carsor = connection.cursor()


employee1 = Employee('Junayed', 'Khan', 20000)
employee2 = Employee('Jabir', 'Khan', 30000)

# insert Data in pythonic way - One
carsor.execute("INSERT INTO employee VALUES (?, ?, ?)", (employee1.first, employee1.last, employee1.pay))
connection.commit()

# carsor.execute("INSERT INTO employee VALUES (?, ?, ?)", (employee2.first, employee2.last, employee2.pay))
# connection.commit()

# insert Data in pythonic way - Two
carsor.execute("INSERT INTO employee VALUES (:first, :last, :pay)",
               {'first': employee2.first, 'last': employee2.last, 'pay': employee2.pay})
connection.commit()

carsor.execute("SELECT * FROM employee WHERE last =:last", {'last': 'Tushar'})
print(carsor.fetchall())
