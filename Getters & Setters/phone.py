from items import Items


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