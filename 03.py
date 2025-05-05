# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    brand = "Tesla"

    # Public method
    def start(self):
        print(f"🚗 {self.brand} is starting... 🔋")

my_car = Car()

# Accessing public variable
print("Brand:", my_car.brand)

my_car.start()
