import csv


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

    @classmethod
    def instantiate_from_csv(cls):
        with open("Items.csv", "r") as rd:
            reader = csv.DictReader(rd)
            items = list(reader)

        for item in items:
            Items(
                name=item.get("name"),
                price=float(item.get("price")),
                quantity=int(item.get("quantity")),
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # __repr__() one of the magic methods that returns a printable representation of an object in Python
    # that can be customized or predefined,
    # i.e. we can also create the string representation of the object according to our needs.
    def __repr__(self):
        return f"Items('{self.name}','{self.price}','{self.quantity}')"


Items.instantiate_from_csv()
print(Items.all_item)
print(Items.is_integer(10.5))
print(Items.is_integer(10.0))

