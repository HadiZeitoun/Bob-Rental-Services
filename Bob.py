#creation project structure"
#create class vehicle
class vehicle:
    def __init__(self,brand,model,year,rental_price_per_day):
        self.brand=brand
        self.model=model
        self.year=year
        self.__rental_price_per_day=rental_price_per_day

def display_info(self):
    return f"{self.brand} {self.model} ({self.year}) - ${self.__rental_price_per_day}/day"


def calculate_cost(self,days):
    return days*self.__rental_price_per_day

def get_price(self):
    return self.__rental_price_per_day

def set_price(self,new_price):
    if new_price>0:
        self.__rental_price_per_day=new_price
    else:
        print("Error: Price must be positive") 

class car(vehicle):
    def __init__(self,brand,model,year,rental_price_per_day,seating_capacity):
        super().__init__(brand,model,year,rental_price_per_day)
        self.seating_capacity=seating_capacity
        
    def display_info(self):
      return super().display_info() + f" - {self.seating_capacity} seats"
  
class bike(vehicle):
    def __init__(self,brand,model,year,rental_price_per_day,engine):
        super().__init__(brand,model,year,rental_price_per_day)
        self.engine=engine
    
    def display_info(self):
        return super().display_info() + f" - Engine: {self.engine}"
    
def display(vehicle):
    vehicle.display_info()
    
car1 = car("Toyota", "Corolla", 2020, 50, 5)
bike1 = bike("Yamaha", "R1", 2019, 30, "998cc")  

display(car1)
display(bike1)

days_car = 3
days_bike = 5
print(f"\n{car1.brand} {car1.model} rental for {days_car} days: ${car1.calculate_cost(days_car)}")
print(f"{bike1.brand} {bike1.model} rental for {days_bike} days: ${bike1.calculate_cost(days_bike)}")

car1.set_price(55)
print(f"\nNew price for {car1.brand} {car1.model}: ${car1.get_price()}/day")
    
    

        


    

        