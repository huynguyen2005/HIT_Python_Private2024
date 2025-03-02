class Manufacturer:
    def __init__(self, identity, location):
        self.identity = identity
        self.location = location
    def describe(self):
        print("Identity: ", self.identity, " - Location: ", self.location)
    
class Device:
    def __init__(self, name, price, manufacturer_identity, manufacturer_location):
        self.name = name
        self.price = price
        self.manufacturer = Manufacturer(manufacturer_identity, manufacturer_location)
    def describe(self):
        print(">>Name: ", self.name, " - Price: ",self.price)
        self.manufacturer.describe()

device1 = Device("mouse", 2.5, 9725, "Vietnam")
device1.describe()
device2 = Device("monitor", 12.5, 11, "Germany")
device2.describe()
        
        