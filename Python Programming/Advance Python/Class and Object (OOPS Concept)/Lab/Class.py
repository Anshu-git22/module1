class Car:
    def setData(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def showData(self):
        print("Car Name:", self.name)
        print("Car Color:", self.color)
        print("Car Price:", self.price)

c1 = Car()
c1.setData("BMW", "Black", 5000000)
c1.showData()