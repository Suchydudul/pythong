
def shipping_label (*args, **kwargs):
    for arg in args:
        print (f"{arg}", end=" ")
    print("")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

shipping_label("Mr.", "Adam", "Smith",
               Street_number="123",
               Street_name = "Fake",
               State="Nowhere")
