# Ask the user what type of conversion they want
print("Press 1 for Celsius to Fahrenheit")
print("Press 2 for Fahrenheit to Celsius")

choice = int(input("Enter your choice: "))

# If user chooses 1, convert Celsius to Fahrenheit
if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

# If user chooses 2, convert Fahrenheit to Celsius
elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Temperature in Celsius:", celsius)

# If user enters any other number
else:
    print("Invalid choice!")