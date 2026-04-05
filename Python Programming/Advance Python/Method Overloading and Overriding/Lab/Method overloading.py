class Food:

    def order(self, item=None):
        if item is None:
            print("Order placed")
        else:
            print("Order placed for", item)

f1 = Food()

f1.order()
f1.order("Pizza")