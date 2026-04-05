discount = 50000

class Car:
    
    def setData(self, name, price):
        final_price = price - discount
        
        self.name = name
        self.price = price
        self.final_price = final_price

    def showData(self):
        print("Car Name:", self.name)
        print("Original Price:", self.price)
        print("Discount:", discount)
        print("Final Price:", self.final_price)

c1 = Car()
c1.setData("BMW", 5000000)
c1.showData()