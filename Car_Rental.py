class vehicle :
    def __init__(self,brand,model,year,rental_price_per_day):
        self.brand=brand
        self.model=model
        self.year=year
        self.__rental_price_per_day=rental_price_per_day
    def get_rental_price_per_day(self):
        return self.__rental_price_per_day
    def set_rental_price_per_day(self,newPrice):
        self.__rental_price_per_day=newPrice
    def display_info(self):
       return(
            f"{self.__class__.__name__}:{self.brand} {self.model},Year:{self.year},"
            f"Renatal Price:${self.__rental_price_per_day}/day"
        )
    def calculateRentalCost(self,Days):
        return Days*int((self.__rental_price_per_day))
class Car(vehicle):
    def __init__(self, brand, model, year, rental_price_per_day,seating_capacity):
        self.seating_capacity=seating_capacity
        super().__init__(brand, model, year, rental_price_per_day)
    def display_info(self):
        temp=super().display_info()
        print(f"{temp},Seats: {self.seating_capacity}")
class Bike(vehicle):
    def __init__(self,brand,model,year,rental_price_per_day,engine_capacity):
        self.engine_capacity=engine_capacity
        super().__init__(brand,model,year,rental_price_per_day)
    def display_info(self):
        temp= super().display_info()
        print(f"{temp},engine_capacity:{self.engine_capacity}c")

def show_vechile_info(vehicle):
    return vehicle.display_info()
        
c1=Car("Toyota","Corolla","2020","50","5")
c1.display_info()
b1=Bike("Yamaha","R1","2019","30","998")
b1.display_info()
print(f"The rantal cost of {c1.brand} {c1.model} for 3 days is :{c1.calculateRentalCost(3)}")
print(f"The rantal cost of {b1.brand} {b1.model} for 3 days is :{b1.calculateRentalCost(5)}")
c1.set_rental_price_per_day(55)
print(f"Updated rental price for {c1.brand} {c1.model} : ${c1.get_rental_price_per_day()}/day")

