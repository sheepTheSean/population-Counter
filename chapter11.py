# Defines the parent class Employee
class Employee():

    # Defines the __init__ function that stores the employee name and number attributes
    def __init__(self, name, number):
        self.__name = name
        self.__number = number
        
    # Defines the mutator and accessor functions for employee name and number
    def set_name(self, name):
        self.__name = name
    def set_number(self, number):
        self.__number = number
    def get_name(self):
        return self.__name
    def get_number(self):
        return self.__number
        
# Defines the child class ProductionWorker
class ProductionWorker(Employee):

    # Defines the child class's __init__ which calls the parent class's __init__ function
    # as well as the shift number and pay rate attributes
    def __init__(self, name, number, shift_number, pay_rate):
        Employee.__init__(self, name, number)
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate
        
    # Defines the mutator and accessor functions for shift_number and pay_rate
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number
    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate
    def get_shift_number(self):
        return self.__shift_number
    def get_pay_rate(self):
        return self.__pay_rate

def main():
    # Recieves user input for various variables used later
    workerName = input("Please input your name: ")
    workerNum = input("Please input your Employee Number: ")
    workerShift = input("Please input your shift(1 for Day Shift, 2 for Night Shift): ")
    workerPay = input("Please input your hourly pay rate: ")
    
    # Creates an instance of the ProductionWorker class using the variables containing user input
    worker = ProductionWorker(workerName, workerNum, workerShift, workerPay)
    
    # Prints the name and employee number, retrieved using the accessor functions from the ProductionWorker class and its parent
    print("Name: ", worker.get_name())
    print("Employee number: ", worker.get_number())
    
    # Prints the shift using if else statements
    if worker.get_shift_number() == 1:
        print("You are in the day shift")
    else:
        print("You are in the night shift")
    
    # Prints the pay rate
    print("Pay rate: ", worker.get_pay_rate())

# Runs the main() function
main()
    
