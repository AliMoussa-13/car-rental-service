class Vechile :
    def __init__(self,brand,model,year,rental_price_per_day):
        self.brand=brand
        self.model=model
        self.year=year
        self.rental_price_per_day=rental_price_per_day
    def display_info(self):
       return(
            f"{self.__class__.__name__}:{self.brand} {self.model},Year:{self.year},"
            f"Renatal Price:{self.rental_price_per_day}"
        )
    def calculateRentalCost(self,Days):
        return Days*int((self.rental_price_per_day))
class Car(Vechile):
    def __init__(self, brand, model, year, rental_price_per_day,seating_capacity):
        self.seating_capacity=seating_capacity
        super().__init__(brand, model, year, rental_price_per_day)
    def display_info(self):
        z=super().display_info()
        print(f"{z},Seats: {self.seating_capacity}")
c1=Car("Toyota","Corolla","2020","50","5")
c1.display_info()