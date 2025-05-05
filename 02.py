# 2. Using cls

# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

    @classmethod
    def show_count(cls):
        print("📦 Total objects created:", cls.count)


# Creating multiple objects
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()

Counter.show_count()
