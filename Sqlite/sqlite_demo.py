import sqlite3
from employee import Employee
connection = sqlite3.connect('employee.db')

carsor = connection.cursor()


# carsor.execute("""  CREATE TABLE employee (
#                         first text,
#                         last text,
#                         pay integer
#
#                         )""")

# insert Data one way
# carsor.execute("INSERT INTO employee VALUES('Abir', 'Tushar', '50000') ")

employee1 = Employee('Junayed', 'Khan', 20000)
employee2 = Employee('Jabir', 'Khan', 30000)

# insert Data in pythonic way
# carsor.execute("INSERT INTO employee VALUES (?, ?, ?)", (employee1.first, employee1.last, employee1.pay))
# connection.commit()

carsor.execute("INSERT INTO employee VALUES (?, ?, ?)", (employee2.first, employee2.last, employee2.pay))
# connection.commit()

carsor.execute("INSERT INTO employee VALUES (:first, :last, :pay)",
               {'first': employee1.first, 'last': employee1.last, 'pay': employee1.pay})
connection.commit()
# to delete row wise
# carsor.execute("DELETE FROM employee WHERE rowid = '7'")

# to delete all the table
# carsor.execute("DELETE FROM employee")

carsor.execute("SELECT * FROM employee WHERE last = 'Khan'")
print(carsor.fetchall())
# to see row id and specific value
# carsor.execute("SELECT rowid, first, last FROM employee")

# carsor.execute("SELECT * FROM employee")
# print(carsor.fetchall())

carsor.execute("SELECT * FROM employee WHERE last =:last", {'last': 'Tushar'})
print(carsor.fetchall())

# carsor.execute(("S ELECT"))

connection.commit()
connection.close()