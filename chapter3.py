print('Reboot the computer and try to connect.')
# Asks the user to reboot
response = input('Did that fix the problem? ')
# Prompts the user to see if it fixed the problem and assigns the input to the response variable
if response == 'Yes' or 'yes':
# Runs a decision structure to see if the response gives was Yes or no
# If the response is yes it prints a message then ends the program
    print('The Problem has been fixed')
    exit()
else:
# if the given response is anything other than Yes it prints a new message then continues
    print('Reboot the router and try to connect.')
response = input('Did that fix the problem? ')
# Repeats the process over again
if response == 'Yes' or 'yes':
    print('The Problem has been fixed')
    exit()
else:
    print('Make sure the cables between the router & modem are plugged in firmly.')
response = input('Did that fix the problem? ')
if response == 'Yes' or 'yes':
    print('The Problem has been fixed')
    exit()
else:
    print('Move the router to a new location and try to connect.')
response = input('Did that fix the problem? ')
if response == 'Yes' or 'yes':
    print('The Problem has been fixed')
    exit()
else:
    print('Get a new router.')
# If the problem still isn't fixed the program prints a message then ends
exit()
