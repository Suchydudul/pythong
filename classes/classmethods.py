class employee:
    count = 0
    def __init__(self, name, position):
        self.name = name 
        self.position = position
        employee.count += 1
    #instance method
    def get_info(self):
        return f"The name is {self.name} he/she is a {self.position}, there are {employee.count} employees"
    @classmethod
    def get_count(cls):
        return f"Total # of employees: {cls.count}"

print(employee.get_count())
employee1 = employee("adam", "scammer")

print(employee1.get_info())