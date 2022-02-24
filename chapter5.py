# Defines the main function
def main():

	# Calls the intro function
	intro()
	
	# Retrieves the input for value 1 & 2
	value1 = int(input('Integer #1: '))
	value2 = int(input('Integer #2: '))
	
	# Calls the max function with the variables value1 and value2
	max(value1,value2)

# Defines the max function
def max(num1,num2):
	
	# Checks if num1 is greater than num2
	if num1 > num2:
	
		# Prints the the results of the check
		print(f'{num1} is greater than {num2}.')
		
	# Checks if num2 is greater than num1
	elif num1 < num2:
	
		# Prints the the results of the check
		print(f'{num2} is greater than {num1}.')
	
	# Checks if num1 is equal to num2
	elif num1 == num2:
		
		# Prints the the results of the check
		print(f'{num1} and {num2} are equal.')

# Defines the intro function
def intro():

	# Prints the intro text
	print('Please input 2 separate integers for comparison.')

#Calls the main function
main()
