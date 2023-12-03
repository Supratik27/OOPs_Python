# How to create a class:
class Items:
    def calculate_total_Price(self, x, y):
        return x * y


# How to create an instance of a class
ItemA = Items()
# Assign attributes:
ItemA.name = "Laptop"
ItemA.price = 60000
ItemA.quantity = 5
# Calling methods from instances of a class:
print("The total price is Rs %d" % ItemA.calculate_total_Price(ItemA.quantity, ItemA.price))
