# 4. Class Variables and Class Methods

# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Global Bank"

    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
        print(f"Bank name has been changed to {cls.bank_name}")

# Creating multiple instances of Bank
bank1 = Bank()
bank2 = Bank()

# Displaying the initial bank name
print("Initial bank name for bank1:", bank1.bank_name)
print("Initial bank name for bank2:", bank2.bank_name)

# Changing the bank name using class method
Bank.change_bank_name("Tech Bank")

# Displaying the updated bank name
print("Updated bank name for bank1:", bank1.bank_name)
print("Updated bank name for bank2:", bank2.bank_name)
