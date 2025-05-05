# 6. Constructors and Destructors

# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

class Logger:
    def __init__(self):
        # Constructor: Called when the object is created
        print("Logger object created!")

    def __del__(self):
        # Destructor: Called when the object is destroyed
        print("Logger object destroyed!")

# Creating an object of Logger
log = Logger()


del log  
