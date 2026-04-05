class Device:
    def info(self):
        print("This is a device")

class Mobile(Device):
    def info(self):
        super().info()
        print("This is a mobile")

class Laptop(Device):
    def info(self):
        super().info()
        print("This is a laptop")

class SmartDevice(Mobile, Laptop):
    def info(self):
        super().info()
        print("This is a smart device")

d1 = SmartDevice()
d1.info()