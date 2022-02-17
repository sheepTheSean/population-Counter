
# Retrieves the value for the number of starting organisms and places it into the 'organism' variable
organism = int(input('Starting number of organisms: '))

# Retrieves the value for the Average daily increase and places it into the 'dailyIncrease' variable
dailyIncrease = (int(input('Average daily percent increase: ')))/100

# Retrieves the value for the number of days needed and places it into the 'days' variable
days = int(input('Number of days to multiply: '))

# prints a blank space to make room
print()

# prints the title of the table
print('Day Approximate\t|\tPopulation')
print('----------------------------------')

# Sets a loop using a range equal to the amount of days input by the user
for counter in range(days):

    # Gets the current day to be printed correctly on the screen. Adds 1 to correct for starting at 0
    currentDay = int(counter+1)

    # Adds its previous value * the percentage increase
    organism += dailyIncrease*(organism)
    # prints the data for the table every time the loop repeats
    print(f'{currentDay}\t\t|\t{organism}')
    

