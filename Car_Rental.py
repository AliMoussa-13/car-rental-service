class Vechile :
    def __init__(self,brand,model,year,rental_price_per_day):
        self.brand=brand
        self.model=model
        self.year=year
        self.rental_price_per_day=rental_price_per_day
    def display_info(self):
        print(
        f"The vechile has the following properties:"
        f" (brand): {self.brand}"
        f" (model):{self.model}"
        f" (year): {self.year}"
        f" (rental price per day):{self.rental_price_per_day}"
        )
    def calculateRentalCost(self,Days):
        return Days*int((self.rental_price_per_day))
    
        
v1=Vechile("BMW","M5","2005","30")
v1.display_info()
z=v1.calculateRentalCost(3)
print(z)
