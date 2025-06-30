class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    def drive(self):
        print(f"Your drive the {self.model}")

car1=Car("Ferrari", 2020, "red", False)
car2=Car("corvette",2022,"blue", True)

car2.drive()
