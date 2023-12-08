from items import Items
from phone import Phone

Item12 = Items("RAM", 3500)
print(Item12.name)

# Setting an attribute
Item12.name = "Car"
# Getting an attribute
print(Item12.name)
# Setting another attribute
Item13 = Items("Robot", 3700)
print(Item13.price)
# Setting increment value
Item13.apply_increment(0.7)
print(Item13.price)
print(Item13.send_email())
PhoneA = Phone("Iphone14", 170000)
# We can observe that the object of the class "Phone" can use the method in its parent class "Items"
PhoneA.send_email()
PhoneA.apply_increment(0.5)
print(PhoneA.price)
PhoneA.apply_discount()
print(PhoneA.price)