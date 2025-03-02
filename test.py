class Vehicle:
    def __init__(self, brand, model, year, price_per_day):
        self.brand = brand
        self.model = model
        self.year = year
        self.__price_per_day = price_per_day

    def show_info(self):
        print(f"{self.brand} {self.model} ({self.year}) - ${self.__price_per_day}/day")

    def calculate_cost(self, days):
        return days * self.__price_per_day

    def get_price(self):
        return self.__price_per_day

    def set_price(self, new_price):
        if new_price > 0:
            self.__price_per_day = new_price
        else:
            print("Error: Price must be positive")


class Car(Vehicle):
    def __init__(self, brand, model, year, price_per_day, seats):
        super().__init__(brand, model, year, price_per_day)
        self.seats = seats

    def show_info(self):
        print(f"Car: {self.brand} {self.model} ({self.year}) - {self.seats} seats, ${self.get_price()}/day")


class Bike(Vehicle):
    def __init__(self, brand, model, year, price_per_day, engine):
        super().__init__(brand, model, year, price_per_day)
        self.engine = engine

    def show_info(self):
        print(f"Bike: {self.brand} {self.model} ({self.year}) - Engine: {self.engine}, ${self.get_price()}/day")


def display(vehicle):
    vehicle.show_info()


car1 = Car("Toyota", "Corolla", 2020, 50, 5)
bike1 = Bike("Yamaha", "R1", 2019, 30, "998cc")  

display(car1)
display(bike1)

days_car = 3
days_bike = 5
print(f"\n{car1.brand} {car1.model} rental for {days_car} days: ${car1.calculate_cost(days_car)}")
print(f"{bike1.brand} {bike1.model} rental for {days_bike} days: ${bike1.calculate_cost(days_bike)}")

car1.set_price(55)
print(f"\nNew price for {car1.brand} {car1.model}: ${car1.get_price()}/day")                                                         