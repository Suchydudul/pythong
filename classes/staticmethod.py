class employee:
    def __init__(self, name, position):
        self.name = name 
        self.position = position

    def get_info(self):
        return f"The name is {self.name} he/she is a {self.position}"
    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager","Cook", "Cashier"]
        return position in valid_position
print(employee.is_valid_position("Cook"))