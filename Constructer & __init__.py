class Items:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"The price of the item {name} should be greater than equal to zero"
        assert quantity >= 0, f"The quantity of the item {name} should be greater than equal to zero"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_Price(self):
        return f"The total price of the item {self.name} is Rs:", self.price * self.quantity


# Assign attributes:
Item1 = Items("Bicycle", 3, 1500)
print(Item1.calculate_total_Price())
Item2 = Items("Car", 1, 1500000)
print(Item2.calculate_total_Price())
