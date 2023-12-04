class Items:
    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"The price of the items is {price} should be greater than equal to zero"
        assert quantity >= 0, f"The quantity of the items is {quantity} should be greater than equal to zero"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_Price(self):
        return f"the total price of the {self.name} is:", self.price * self.quantity


Item1 = Items("Skateboard", 2, 2500)
Item2 = Items("Bike", 1, 65000)
print(Item1.calculate_total_Price())
print(Item2.calculate_total_Price())

