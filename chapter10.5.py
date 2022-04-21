# Defines a class called RetainItem
class RetailItem:
    
    # Defines the __init__ method and sets the description, numberOfUnits, and price as attributes
    def __init__(self, description, numberOfUnits, price):
    
        # accepts arguments for the three attributes and assigns them
        self.description = description
        self.numberOfUnits = numberOfUnits
        self.price = price

# efines the CashRegister class
class CashRegister:
    
    # defines the __init__ method which is set to an empty list
    def __init__(self):
        self.items = []

    # defines the purchase_item method which adds the selected item to the list
    def purchase_item(self, RetailItem):
        self.items.append(RetailItem)

    # defines the get_total method which sets a total variable and runs a for loop
    # to add the items in the list together
    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price
            
        # returns the total variable to the class
        return(total)

    # defines the show_items method which prints the items that are selected in the list
    def show_items(self):
        for item in self.items:
            print(item.description)
            print(item.price)
            print(item.numberOfUnits)

    # clears the selected items in the list
    def clear(self):
        self.items = []
    

# defines the main function
def main():
    
    # sets the item1, item2, and item3 variables to the class object RetailItem
    item1 = RetailItem("Jacket", 12, 59.95)
    item2 = RetailItem("Designer Jeans", 40, 34.95)
    item3 = RetailItem("Shirt", 20, 24.95)
    
    # prints various info
    print("Items available for purchase: ")
    print()
    print(item1.description, item1.numberOfUnits, item1.price)
    print(item2.description, item2.numberOfUnits, item2.price)
    print(item3.description, item3.numberOfUnits, item3.price)
    print()

    # creates an instance of the CashRegister() object
    register = CashRegister()

    # sets a variable to be used later for confirming
    confirmation = "Y"

    # sets an index with the various retail items
    item_list = [item1, item2, item3]

    # sets a while loop only active when confirmation is equal to
    # "Y" to allow for multiple selections
    while confirmation == "Y":

        # sets the user input to a selection variable and then adds the selected
        # item through the index
        selection = input("Which item would you like to purchase? (enter 1, 2, 3):  ")
        register.purchase_item(item_list[int(selection)-1])

        # confirms if the user would like to select another item for purchasing
        confirmation = input("Would you like to purchase another item? (enter Y or N):  ")

    # prints the items in the cart using the show_items() method as well as the total
    print("Items you are purchasing: ")
    print(str(register.show_items()))
    print("$", str(register.get_total()))

    # asks the user if they would clear the cart
    confirmation2 = input("Would you like to clear your cart? (enter Y or N):  ")

    # if the user input is equal to "Y", clears the list using the clear() method
    if confirmation2 == "Y":
        register.clear()

# calls the main function
if __name__ == '__main__':
    main()

