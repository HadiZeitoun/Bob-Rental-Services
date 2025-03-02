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
        


    

        