class Items:
    discount = 0.7  # The discount rate after 30% discount
    all_item = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validations to the received arguments
        assert price >= 0, f"The price of the item {name} should be greater than equal to zero"
        assert quantity >= 0, f"The quantity of the item {name} should be greater than equal to zero"
        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Items.all_item.append(self)

    def calculate_total_Price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Items.discount

    # __repr__() one of the magic methods that returns a printable representation of an object in Python
    # that can be customized or predefined,
    # i.e. we can also create the string representation of the object according to our needs.
    def __repr__(self):
        return f"Items('{self.name}','{self.price}','{self.quantity}')"


Item1 = Items("Pencil", 20, 10)
Item2 = Items("Rubber", 5, 25)
Item3 = Items("TextCopy", 50, 5)
Item4 = Items("Pen", 15, 30)
Item5 = Items("ColourPencil", 10, 35)
Item6 = Items("GeometryBox", 100, 5)

print(Items.all_item)
Item1.apply_discount()
print(Item1.price)
