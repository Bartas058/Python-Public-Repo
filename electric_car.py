class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        full_name = f"{self.make}, {self.model}, {self.year}"
        return full_name.title()
    
    def read_odometer(self):
        print(f"Ten samochód ma przejechane {self.odometer_reading} km.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"Nie można cofnąć licznika przebiegu samochodu.")

    def increament_odomoter(self, kilometres):
        self.odometer_reading += kilometres

class Battery():

    def __init__(self, battery_size = 75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"Ten samochód ma akumulator o pojemności {self.battery_size} kWh.")

    def fill_gas(self):
        print("Ten samochód nie wymaga tankowania paliwa!")

    def get_range(self):

        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"Zasięg tego samochodu wynosi około {range} km, po pełnym naładowaniu akumulatora.")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size += int(100) - self.battery_size
            return self.battery_size

class EletricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = EletricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()