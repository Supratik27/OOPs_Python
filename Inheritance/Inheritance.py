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
        with open("Items2.csv", "r") as It:
            reader1 = csv.DictReader(It)
            items1 = list(reader1)

        for item in items1:
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
        return f"{self.__class__.__name__}('{self.name}','{self.price}','{self.quantity}')"


class Phone(Items):

    def __init__(self, name: str, price: float, quantity=0, broken_phone=0):
        # Call to super function to have access to all attributes / methods of the parent class
        super().__init__(
            name, price, quantity
        )
        # Run validations to the received arguments
        assert broken_phone >= 0, f"The quantity of the broken phone of the item {name} should be greater than equal to zero"
        # Assign to self object
        self.broken_phone = broken_phone


phoneA = Phone("Samsung", 15000, 4, 1)
phoneA.apply_discount()
print(phoneA.calculate_total_Price())
print(Items.all_item)
