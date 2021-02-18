class Employee:

    def __init__(self, name, nid):
        self.name = name
        self.nid = nid
        self.laptop = self.Laptop

    def show_details(self):
        print(self.name, self.nid)

    class Laptop:

        def __init__(self):
            self.brand = 'Lenovo'
            self.core = 'i7'
            self.ram = 8

        def show_detail(self):
            print(self.brand, self.core, self.ram)


employee = Employee('Tushar', '38687...')
employee.show_details()

lap1 = Employee.Laptop()
lap1.show_detail()
# print(lap1)
