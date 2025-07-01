def add_sprinkles(func):
    def wrapper():
        print("*..*:*:*:*..*")
        func()
    return wrapper

@add_sprinkles
def get_ice_cream():
    print("here's your ice cream <8")

get_ice_cream()