class animal:
    def __init__(self,name,age):
        self.age = age
        self.name = name

    def eat(self):
        print(f"{self.name} eats")
    
    def sleep(self):
        print(f"{self.name} sleeps")

class cat(animal):
    pass

class human(animal): 

    def write(self):
        print(f"{self.name} is writing a book")

human1= human("james", 24)
cat1 = cat("larry", 3)

cat1.eat()
human1.sleep()
human1.write()